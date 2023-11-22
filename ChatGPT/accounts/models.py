from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.
class UserQuiz(models.Model):
    user_id = models.ForeignKey(User, verbose_name=_("유저 아이디"), on_delete=models.CASCADE)
    recently_quiz = models.DateField(_("퀴즈 푼 최근날짜"), auto_now_add=True)
    today_quiz = models.PositiveSmallIntegerField(_("퀴즈 푼 수"), default=5)
