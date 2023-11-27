from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("register", views.UserCreateAPIView)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.UserLoginView.as_view()),
    path("logout/", views.UserLogoutView.as_view()),
    path("csrf/", views.csrf, name="csrf"),
    # path("signup/", views.logout),
]
