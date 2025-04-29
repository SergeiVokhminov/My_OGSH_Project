from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView, DeleteView

from tasks.models import Task
from users.forms import UserRegisterForm, UserUpdateForm, UserForm
from users.models import User


class UserInfoView(UpdateView):
    """Контроллер просмотра профиля пользователя."""

    model = User
    form_class = UserForm
    template_name = "users/user_info.html"
    success_url = reverse_lazy("users:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_count"] = Task.objects.count()  # Считаем количество пользователей

        return context


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "users/home.html"


class UserRegisterView(CreateView):
    """Контроллер регистрации профиля."""

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


class UserListView(ListView):
    """Контроллер отображения списка пользователей сервиса."""

    model = User
    template_name = "users/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_count"] = User.objects.count() # Считаем количество пользователей

        return context


class UserDetailsView(DetailView):
    """Контроллер отображения профиля пользователя."""

    model = User
    form_class = UserForm
    template_name = "users/user_detail.html"


class UserUpdateView(UpdateView):
    """Контроллер обновления профиля пользователя."""

    model = User
    form_class = UserUpdateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:home")


class UserDeleteView(DeleteView):
    """Контроллер удаления профиля пользователя."""

    model = User
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy(
        "users:home"
    )

    def test_func(self):
        return (
            self.request.user.is_staff
        )  # Только администраторы могут удалять пользователей

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs["pk"])
