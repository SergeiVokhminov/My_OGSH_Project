from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    HomeView, UserRegisterView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="users:home"), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
