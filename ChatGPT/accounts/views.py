from django.shortcuts import render

# django views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

# DRF
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# costom py
from .models import User, UserQuiz
from .serializers import UserSerializer

# from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserQuiz.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = self.request.data.get("password")  # type: ignore
        print(self.request.data)
        if password:
            user = serializer.save()
            user.set_password(password)
            user.save()
        else:
            return Response(
                {"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST
            )
