from django.db import models
from accounts.models import User
from django.utils.translation import gettext as _


class Quiz(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    solved_at = models.DateTimeField(auto_now_add=True, verbose_name="문제 푼 날짜")
    prompt = models.TextField(verbose_name="문제")
    response = models.TextField(verbose_name="답변")
    correct = models.BooleanField(verbose_name="정답여부")

    def __str__(self):
        return f"{self.prompt}: {self.response}"
