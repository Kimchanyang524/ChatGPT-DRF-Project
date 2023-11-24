from django.shortcuts import render

# django views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth import authenticate

# DRF
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

# costom py
from .models import User, UserQuiz
from .serializers import UserSerializer

# from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserQuiz.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = self.request.data.get("password")  # type: ignore
        if password:
            user = serializer.save()
            user.set_password(password)
            user.save()
        else:
            return Response(
                {"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token) # type: ignore

        return Response(
            {
                'message': "로그인 성공",
                'access_token': access_token
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {'message': '로그인 실패! 아이디 또는 비밀번호를 확인하세요.'},
            status=status.HTTP_200_OK
        )

@api_view(['POST'])
def logout(request):
    return Response(
        {
            'message': "로그아웃 성공",
            'token_delete': True
        },
        status=status.HTTP_200_OK)