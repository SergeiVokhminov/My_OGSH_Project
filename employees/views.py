from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from employees.models import Employee
from employees.forms import EmployeeForm, EmployeeUpdateForm
from employees.utils import EmployeeCounter
from tasks.utils import TaskCounter


class EmployeeCreateView(CreateView):
    """Контроллер добавления пользователя на сайт."""

    model = Employee
    form_class = EmployeeUpdateForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees:employee_list.html")

    def form_valid(self, form):
        employee = form.save()
        user = self.request.user
        employee.owner = user
        employee.save()
        return super().form_valid(form)

    def test_func(self):
        """Проверка, является ли пользователь суперпользователем."""

        return self.request.user.is_superuser


class EmployeeInfoView(UpdateView):
    """Контроллер просмотра профиля пользователя."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_info.html"
    success_url = reverse_lazy("home_page:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter_employee = EmployeeCounter()
        counter_task = TaskCounter()

        context["employee_count"] = counter_employee.total()  # Считаем общее количество пользователей
        context["employee_at_work_count"] = (
            counter_employee.at_work
        )  # Считаем количество пользователей со статусом "На работе"
        context["employee_on_vacation_count"] = (
            counter_employee.on_vacation
        )  # Считаем количество пользователей со статусом "В отпуске"
        context["employee_on_sick_leave_count"] = (
            counter_employee.on_sick_leave
        )  # Считаем количество пользователей со статусом "На больничном"
        context["employee_truancy_count"] = (
            counter_employee.truancy
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


class EmployeeListView(ListView):
    """Контроллер отображения списка пользователей сервиса."""

    model = Employee
    template_name = "employees/employee_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # counter = UserCounter()
        #
        # # Используем свойства или методы класса UserCounter
        # context["user_count"] = counter.total()  # Считаем количество пользователей
        # context["user_at_work_count"] = (
        #     counter.at_work
        # )  # Считаем количество пользователей "На работе"
        # context["user_on_vacation_count"] = (
        #     counter.on_vacation
        # )  # Считаем количество пользователей "В отпуске"
        # context["user_on_sick_leave_count"] = (
        #     counter.on_sick_leave
        # )  # Считаем количество пользователей "На больничном"
        # context["user_truancy_count"] = (
        #     counter.truancy
        # )  # Считаем количество пользователей "Прогул"

        return context


class EmployeeDetailsView(DetailView):
    """Контроллер отображения профиля пользователя."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_detail.html"


class EmployeeUpdateView(UpdateView):
    """Контроллер обновления профиля пользователя."""

    model = Employee
    form_class = EmployeeUpdateForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("home_page:home")


class EmployeeDeleteView(DeleteView):
    """Контроллер удаления профиля пользователя."""

    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("home_page:home")

    def test_func(self):
        return (
            self.request.user.is_staff
        )  # Только администраторы могут удалять пользователей

    def get_object(self, queryset=None):
        return get_object_or_404(Employee, pk=self.kwargs["pk"])
