from rest_framework.serializers import ModelSerializer
from .models import Quiz
from django.contrib.auth import get_user_model


class QuizSerializer(ModelSerializer):
    """
    퀴즈의 내역을 출력한다.
    """

    class Meta:
        model = Quiz
        fields = [
            "prompt",
            "response",
            "correct",
        ]
