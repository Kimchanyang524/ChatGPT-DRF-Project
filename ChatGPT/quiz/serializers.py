from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import get_user_model


class QuizSerializer(ModelSerializer):
    """
    퀴즈의 내역을 출력한다.
    """

    class Meta:
        model = User
        fields = [
            "prompt",
            "response",
        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
