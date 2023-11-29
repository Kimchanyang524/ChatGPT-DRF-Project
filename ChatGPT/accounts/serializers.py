from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    """
    사용자 아이디(username)와 비밀번호(password)를 받는 직렬화 클래스
    """

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
