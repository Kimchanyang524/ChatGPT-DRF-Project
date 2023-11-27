from django.db import models
from accounts.models import User
from django.utils.translation import gettext as _


class Quiz(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("사용자"))
    solved_at = models.DateTimeField(_("문제 푼 날짜"), auto_now_add=True)
    prompt = models.TextField()
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"
