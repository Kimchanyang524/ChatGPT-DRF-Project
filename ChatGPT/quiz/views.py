# django base
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils import timezone
from django.conf import settings

# rest framework
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# custom py
from accounts.models import User, UserQuiz
from accounts.serializers import UserSerializer
from accounts.permissions import IsNotAuthenticated
from .models import Quiz
from .serializers import QuizSerializer
from .permissions import AllAccess

# openai
import openai

# python base
from dotenv import load_dotenv
import os
import jwt
from datetime import datetime

load_dotenv()
secret_key = settings.SECRET_KEY


class ChatBotAPIView(APIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsNotAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        퀴즈 문제를 출제하는 기능
        """
        client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """
                    너는 이제부터 랜덤한 영어단어를 하나 말해주는 기계야.
                    영어 단어를 말할떄는 반드시 앞뒤에 *을 붙여서 말하고 그 이외에는 *을 사용하면 안돼
                    영어 단어의 한국어 뜻은 반드시 앞뒤에 #을 붙여서 말하고 그 이외에는 #을 사용하면 안돼
                    """,
                }
            ],
            model="gpt-3.5-turbo",
        )
        content = chat_completion.choices[0].message.content
        return Response({"content": content})

    def post(self, request):
        """
        퀴즈 푼 기록을 남기는 기능
        """
        today = datetime.now().date()
        question = request.data.get("question")
        answer = request.data.get("answer")
        correct = request.data.get("correct")
        Quiz.objects.create(
            user_id=request.user,
            prompt=question,
            response=answer,
            correct=correct,
        )
        userquiz = UserQuiz.objects.filter(user_id=request.user).first()

        # 퀴즈 데이터가 있으면 갱신한다.
        if userquiz:
            if userquiz.recently_quiz == today:
                userquiz.today_quiz += 1
            else:
                userquiz.today_quiz = 1
                userquiz.recently_quiz = today
            userquiz.save()
            if userquiz.today_quiz >= 5:
                return Response({"redirect": True})
        return Response({})


class QuizAPIView(APIView):
    def get(self, request):
        quiz = Quiz.objects.filter(user_id=request.user)
        serializer = QuizSerializer(quiz, many=True)
        return Response({"serializer": serializer.data})
