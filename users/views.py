from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.models import User


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "users/home.html"


class UserRegisterView(CreateView):
    """Контроллер регистрации профиля."""

    model = User
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")