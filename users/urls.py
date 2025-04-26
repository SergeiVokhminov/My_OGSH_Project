from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    HomeView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
