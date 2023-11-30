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
    """
    챗봇 기능이 담긴 View이다.

    function:
    - get: 챗봇 요청
    - post: 퀴즈 질문과 답변, 정답여부를 데이터베이스에 저장
    """

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        퀴즈 문제를 출제하는 기능

        header:
        - Authorization: Bearer token

        return:
        - content: ChatGPT의 답변
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

        header:
        - Authorization: Bearer token

        args:
        - question: 문제
        - answer: 사용자의 답변
        - correct: 정답여부

        return:
        - redirect: True
        - None

        error:
        - HTTP 400 Bad Request
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
        print(1)
        print(userquiz)

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
        return Response(status=status.HTTP_400_BAD_REQUEST)


class QuizAPIView(APIView):
    """
    역대 퀴즈 기록을 출력하는 클래스이다

    function:
    - get: 전체 기록 출력
    """

    def get(self, request):
        """
        로그인한 유저의 전체 퀴즈 기록을 출력하는 기능이다.

        header:
        - Authorization: Bearer token

        return:
        - serializer: 전체 퀴즈 기록이 JSON으로 전송된다.
        """
        quiz = Quiz.objects.filter(user_id=request.user)
        serializer = QuizSerializer(quiz, many=True)
        return Response({"serializer": serializer.data})
