from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.QuizAPIView.as_view()),
    path("chat/", views.ChatBotAPIView.as_view()),
]
