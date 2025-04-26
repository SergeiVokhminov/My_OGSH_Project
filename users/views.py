from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from users.models import User


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "users/home.html"


class UserRegisterView(CreateView):
    """Контроллер регистрации профиля."""

    model = User
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


class UserDetailsView(DetailView):
    """Контроллер отображения профиля пользователя."""

    model = User
    template_name = "users/user_detail.html"


class UserUpdateView(UpdateView):
    """Контроллер обновления профиля пользователя."""

    model = User
    template_name = "users/test.html"
    success_url = reverse_lazy("users:home")
