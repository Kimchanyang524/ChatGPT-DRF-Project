from django.shortcuts import render

# django views
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token

# rest framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# costom py
from .models import User, UserQuiz
from .serializers import UserSerializer
from .permissions import IsNotAuthenticated, PostOnlyAccess


class UserCreateAPIView(viewsets.ModelViewSet):
    """
    인증되지 않은 사용자를 위한 회원가입 엔드포인트를 제공하는 클래스입니다.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    permission_classes = [PostOnlyAccess]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)  # type: ignore

            return Response(
                {
                    "message": "성공적으로 로그인되었습니다!",
                    "access_token": access_token,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "로그인 실패! 아이디 또는 비밀번호를 확인하세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLogoutView(APIView):
    permission_classes = [PostOnlyAccess]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            return Response({"token_delete": True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "Error:": str(e),
                    "token_delete": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


def csrf(request):
    """
    csrf token 발행
    """
    token = get_token(request)
    return JsonResponse({"csrftoken": token})
