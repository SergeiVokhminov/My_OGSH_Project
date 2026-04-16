import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    TemplateView,
)

from users.forms import UserAuthForm, UserRegisterForm
from users.models import User


class UserLoginView(LoginView):
    """Контроллер для входа на сайт."""

    model = User  # Указываем какую модель использовать
    form_class = UserAuthForm  # Указываем какую форму использовать для регистрации
    template_name = "users/login.html"  # Указываем путь к шаблону страницы для входа
    success_url = reverse_lazy(
        "home_page:home"
    )  # Указываем URL, на который будет перенаправлен пользователь после успешного входа
    redirect_authenticated_user = (
        True  # Перенаправлять аутентифицированных пользователей
    )


class UserRegisterView(CreateView):
    """Контроллер регистрации профиля."""

    model = User  # Указываем какую модель использовать
    form_class = UserRegisterForm  # Указываем какую форму использовать для регистрации
    template_name = (
        "users/register.html"  # Указываем путь к шаблону страницы для регистрации
    )
    success_url = reverse_lazy(
        "users:register_success"
    )  # Указываем URL, на который будет перенаправлен пользователь после успешной регистрации

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # Деактивируем до подтверждения почты
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение регистрации на сайте.",
            message=f"Привет, гость! Для активации Вашего аккаунта перейдите по ссылке: {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[
                user.email,
            ],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Функция для верификации почты."""

    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class RegistrationSuccessView(TemplateView):
    template_name = "users/register_success.html"
