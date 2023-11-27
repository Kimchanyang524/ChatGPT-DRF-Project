# django base
from django.shortcuts import render
from django.views import View
from django.utils import timezone

# rest framework
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# custom py
from .models import Quiz
from .serializers import QuizSerializer
from .permissions import AllAccess

# openai
import openai

# python base
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatBotAPIView(APIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get(self, request, *args, **kwargs):
        print("1")
        quizlist = Quiz.objects.filter(user_id=request.user)
        serializer = QuizSerializer(quizlist, many=True)
        return Response({"serializer": serializer.data})

    def post(self, request):
        today = timezone.now().date()
        today_quiz = Quiz.objects.filter(user_id=request.user, solved_at__date=today)
        serializer = QuizSerializer(data=request.data)
        prompt = serializer.data
        if today_quiz:
            for i in today_quiz:
                print(i)
        #     today_quizs = "\n".join(
        #         [f"User: {c.}\nAI: {c['response']}" for c in today_quiz]
        #     )
        #     prompt_with_previous = f"{today_quizs}\nUser: {prompt}\nAI:"

        #     model_engine = "text-davinci-003"
        #     completions = openai.Completion.create(
        #         engine=model_engine,
        #         prompt=prompt_with_previous,
        #         max_tokens=1024,
        #         n=5,
        #         stop=None,
        #         temperature=0.5,
        #     )
        #     response = completions.choices[0].text.strip()

        #     conversation = {"prompt": prompt, "response": response}
        # serializer = QuizSerializer(data=request.data)
