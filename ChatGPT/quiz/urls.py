from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path("list/", views.QuizAPIView.as_view()),
    path("chat/", views.ChatBotAPIView.as_view()),
]
