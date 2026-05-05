from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    RegistrationSuccessView,
    UserLoginView,
    UserRegisterView,
    email_verification, UserForgotPasswordView, UserPasswordResetConfirmView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/", UserLoginView.as_view(template_name="users/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(next_page="home_page:home"), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("email_confirm/<str:token>/", email_verification, name="email_verification"),
    path(
        "register-success", RegistrationSuccessView.as_view(), name="register_success"
    ),
    path("password_reset/", UserForgotPasswordView.as_view(), name="password_reset"),
    path("set_new_password/<uidb64>/<token>/", UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
