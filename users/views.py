from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from tasks.models import Task
from users.forms import UserForm, UserRegisterForm, UserUpdateForm, UserAuthForm
from users.models import User


class UserInfoView(UpdateView):
    """Контроллер просмотра профиля пользователя."""

    model = User
    form_class = UserForm
    template_name = "users/user_info.html"
    success_url = reverse_lazy("users:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_count"] = Task.objects.count()  # Считаем количество задач
        context["start_task_count"] = Task.objects.filter(
            status="start"
        ).count()  # Считаем количество задач "К исполнению"
        context["free_task_count"] = Task.objects.filter(
            status="free"
        ).count()  # Считаем количество задач, статус "Свободна"
        context["done_task_count"] = Task.objects.filter(
            status="done"
        ).count()  # Считаем количество задач, статус "Завершена"
        context["closed_task_count"] = Task.objects.filter(
            status="closed"
        ).count()  # Считаем количество задач "Отменена"

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


class UserLoginView(LoginView):
    """Контроллер для входа на сайт."""

    model = User
    form_class = UserAuthForm
    template_name = "users/login.html"  # Указываем путь к шаблону для входа
    success_url = reverse_lazy(
        "users:home"
    )  # Указываем URL, на который будет перенаправлен пользователь после успешного входа
    redirect_authenticated_user = (
        True  # Перенаправлять аутентифицированных пользователей
    )

    def form_valid(self, form):
        """Обрабатывает успешный вход пользователя."""

        user = form.get_user()
        login(self.request, user)
        messages.success(
            self.request, "Вы успешно вошли в систему."
        )  # Сообщение об успешном входе
        return super().form_valid(form)

    def form_invalid(self, form):
        """Обрабатывает случай, если форма невалидна."""

        messages.error(
            self.request, "Неправильное имя пользователя или пароль."
        )  # Сообщение об ошибке
        return super().form_invalid(form)


class UserListView(ListView):
    """Контроллер отображения списка пользователей сервиса."""

    model = User
    template_name = "users/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_count"] = User.objects.count()  # Считаем количество пользователей
        context["user_at_work_count"] = User.objects.filter(
            condition="work"
        ).count()  # Считаем количество пользователей "На работе"
        context["user_on_vacation_count"] = User.objects.filter(
            condition="vacation"
        ).count()  # Считаем количество пользователей "В отпуске"
        context["user_on_sick_leave_count"] = User.objects.filter(
            condition="sick_leave"
        ).count()  # Считаем количество пользователей "На больничном"
        context["user_truancy_count"] = User.objects.filter(
            condition="truancy"
        ).count()  # Считаем количество пользователей "Прогул"

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
    success_url = reverse_lazy("users:home")

    def test_func(self):
        return (
            self.request.user.is_staff
        )  # Только администраторы могут удалять пользователей

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs["pk"])
