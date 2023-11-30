from django.urls import path
from rest_framework_simplejwt.views import token_refresh, token_verify
from . import views


urlpatterns = [
    path("auth/", views.AuthAPIView.as_view()),
    path("register/", views.UserCreateAPIView.as_view()),
    path("refresh_token/", token_refresh, name="token_refresh"),
    path("verify/", token_verify, name="token_verify"),
]
