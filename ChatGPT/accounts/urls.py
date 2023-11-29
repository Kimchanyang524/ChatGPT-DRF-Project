from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import token_refresh, token_verify
from . import views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", views.AuthAPIView.as_view()),
    path("register/", views.UserCreateAPIView.as_view()),
    path("refresh_token/", token_refresh, name="token_refresh"),
    path("verify/", token_verify, name="token_verify"),
]
