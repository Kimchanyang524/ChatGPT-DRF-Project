from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
