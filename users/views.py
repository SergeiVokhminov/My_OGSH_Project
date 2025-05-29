import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from applications.utils import ApplicationCounter
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

        context["user_count"] = counter_user.total()  # Считаем общее количество пользователей
        context["user_at_work_count"] = (
            counter_user.at_work
        )  # Считаем количество пользователей со статусом "На работе"
        context["user_on_vacation_count"] = (
            counter_user.on_vacation
        )  # Считаем количество пользователей со статусом "В отпуске"
        context["user_on_sick_leave_count"] = (
            counter_user.on_sick_leave
        )  # Считаем количество пользователей со статусом "На больничном"
        context["user_truancy_count"] = (
            counter_user.truancy
        )  # Считаем количество пользователей со статусом "Прогул"

        context["task_count"] = (
            counter_task.total()
        )  # Считаем общее количество созданных задач
        context["start_task_count"] = (
            counter_task.start_task
        )  # Считаем количество задач со статусом "К исполнению"
        context["free_task_count"] = (
            counter_task.free_task
        )  # Считаем количество задач со статусом "Свободна"
        context["done_task_count"] = (
            counter_task.done_task
        )  # Считаем количество задач со статусом "Завершена"
        context["closed_task_count"] = (
            counter_task.closed_task
        )  # Считаем количество задач со статусом "Отменена"

        return context


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "users/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter_user = UserCounter()
        counter_task = TaskCounter()
        counter_application = ApplicationCounter()
        context["greeting"] = TimeGreeting.get_greeting()  # Применяем класс приветствия
        context["user_at_work_count"] = (
            counter_user.at_work
        )  # Считаем количество пользователей "На работе"
        context["start_task_count"] = (
            counter_task.start_task
        )  # Считаем количество задач "К исполнению"
        context["free_task_count"] = (
            counter_task.free_task
        )  # Считаем количество задач "Свободна" application_count
        context["application_count"] = (
            counter_application.total # Считаем общее количество заявок
        )
        return context


class UserRegisterView(CreateView):
    """Контроллер регистрации профиля."""

    # model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение регистрации.",
            message=f"Для активации Вашего аккаунта перейдите по ссылке: {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email,],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Функция для верификации почты."""

    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


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
