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

from tasks.utils import TaskCounter
from users.forms import UserAuthForm, UserForm, UserRegisterForm, UserUpdateForm
from users.models import User
from users.utils import TimeGreeting, UserCounter


class UserInfoView(UpdateView):
    """Контроллер просмотра профиля пользователя."""

    model = User
    form_class = UserForm
    template_name = "users/user_info.html"
    success_url = reverse_lazy("users:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter_user = UserCounter()
        counter_task = TaskCounter()

        context["user_count"] = counter_user.total()  # Считаем количество пользователей
        context["user_at_work_count"] = (
            counter_user.at_work
        )  # Считаем количество пользователей "На работе"
        context["user_on_vacation_count"] = (
            counter_user.on_vacation
        )  # Считаем количество пользователей "В отпуске"
        context["user_on_sick_leave_count"] = (
            counter_user.on_sick_leave
        )  # Считаем количество пользователей "На больничном"
        context["user_truancy_count"] = (
            counter_user.truancy
        )  # Считаем количество пользователей "Прогул"

        context["task_count"] = (
            counter_task.total()
        )  # Считаем общее количество созданных задач
        context["start_task_count"] = (
            counter_task.start_task
        )  # Считаем количество задач "К исполнению"
        context["free_task_count"] = (
            counter_task.free_task
        )  # Считаем количество задач "Свободна"
        context["done_task_count"] = (
            counter_task.done_task
        )  # Считаем количество задач "Завершена"
        context["closed_task_count"] = (
            counter_task.closed_task
        )  # Считаем количество задач "Отменена"

        return context


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "users/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter_user = UserCounter()
        counter_task = TaskCounter()
        context["greeting"] = TimeGreeting.get_greeting()  # Применяем класс приветствия
        context["user_at_work_count"] = (
            counter_user.at_work
        )  # Считаем количество пользователей "На работе"
        context["start_task_count"] = (
            counter_task.start_task
        )  # Считаем количество задач "К исполнению"
        context["free_task_count"] = (
            counter_task.free_task
        )  # Считаем количество задач "Свободна"

        return context


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


class UserListView(ListView):
    """Контроллер отображения списка пользователей сервиса."""

    model = User
    template_name = "users/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter = UserCounter()

        # Используем свойства или методы класса UserCounter
        context["user_count"] = counter.total()  # Считаем количество пользователей
        context["user_at_work_count"] = (
            counter.at_work
        )  # Считаем количество пользователей "На работе"
        context["user_on_vacation_count"] = (
            counter.on_vacation
        )  # Считаем количество пользователей "В отпуске"
        context["user_on_sick_leave_count"] = (
            counter.on_sick_leave
        )  # Считаем количество пользователей "На больничном"
        context["user_truancy_count"] = (
            counter.truancy
        )  # Считаем количество пользователей "Прогул"

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
