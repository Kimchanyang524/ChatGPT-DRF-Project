# django base
from django.shortcuts import render, get_object_or_404
from django.conf import settings

# django views
from django.contrib.auth import authenticate

# rest framework
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
import jwt

# costom py
from .models import User, UserQuiz
from .serializers import UserSerializer
from .permissions import IsNotAuthenticated

secret_key = settings.SECRET_KEY


class UserQuizAPIView(viewsets.ModelViewSet):
    queryset = UserQuiz.objects.all()

    def post(self, request):
        """
        해당 유저의 퀴즈 푼 기록을 확인하는 메서드이다.
        """
        access = request.data.get("access")
        payload = jwt.decode(access, secret_key, algorithms=["HS256"])
        pk = payload.get("user_id")
        user = get_object_or_404(User, pk=pk)
        userquiz = UserQuiz.objects.filter(user_id=user).first()


class UserCreateAPIView(CreateAPIView):
    """
    회원가입을하는 View이다.

    function:
    - create: 회원가입
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated]

    def create(self, request):
        """
        회원가입을하는 메서드이다.

        args:
        - username: 아이디
        - password: 비밀번호

        return:
        - access: access token (JWT)
        - refresh: refresh token (JWT)
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print(type(serializer))
            # UserQuiz.objects.create(user_id="")
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthAPIView(APIView):
    """
    유저 정보를 관리하는 View이다.

    function:
    - post: 로그인
    - delete: 로그아웃
    """

    def post(self, request):
        """
        로그인하는 메서드이다.

        args:
        - username: 아이디
        - password: 비밀번호

        return:
        - access: access token (JWT)
        - refresh: refresh token (JWT)

        error:
        - HTTP 400 Bad Request
        """
        # 유저 인증
        user = authenticate(
            request,
            username=request.data.get("username"),
            password=request.data.get("password"),
        )
        # 이미 회원가입 된 유저일 때
        if user:
            serializer = UserSerializer(user)
            # jwt 토큰 접근
            token = RefreshToken.for_user(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "access": access_token,
                    "refresh": refresh_token,
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        로그아웃하는 메서드이다.

        return:
        - message: Logout success
        """
        response = Response(
            {"message": "Logout success"}, status=status.HTTP_202_ACCEPTED
        )
        return response
