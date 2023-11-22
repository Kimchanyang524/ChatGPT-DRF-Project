from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views as MainViews
from accounts import views as AccountsViews
from quiz import views as QuizViews

router = DefaultRouter()
router.register("accounts", AccountsViews.UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
