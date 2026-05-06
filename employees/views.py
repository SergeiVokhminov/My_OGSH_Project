from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView, TemplateView,
)

from employees.forms import EmployeeForm, EmployeeUpdateForm
from employees.models import Employee
from employees.utils import EmployeeCounter
from tasks.utils import TaskCounter


class EmployeeCreateView(CreateView):
    """Контроллер добавления сотрудников на сайт."""

    model = Employee
    form_class = EmployeeUpdateForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees:employee_list")

    def form_valid(self, form):
        employee = form.save(commit=False)
        plain_password = self.request.POST.get('password')
        # Генерируем хеш пароля
        employee.password = make_password(plain_password)
        employee.email = employee.get_email()
        user = self.request.user
        employee.owner = user
        employee.save()
        return super().form_valid(form)

    def test_func(self):
        """Проверка, является ли сотрудник суперпользователем."""

        return self.request.user.is_superuser


class EmployeeInfoView(TemplateView):
    """Контроллер просмотра профиля сотрудника."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_info.html"
    success_url = reverse_lazy("home_page:home")


class EmployeeListView(ListView):
    """Контроллер отображения списка сотрудников сервиса."""

    model = Employee
    template_name = "employees/employee_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter = EmployeeCounter()

        # Используем свойства или методы класса EmployeeCounter
        context["employee_count"] = counter.total()  # Считаем количество сотрудников
        context["employee_at_work_count"] = (
            counter.at_work
        )  # Считаем количество сотрудников "На работе"
        context["employee_on_vacation_count"] = (
            counter.on_vacation
        )  # Считаем количество сотрудников "В отпуске"
        context["employee_on_sick_leave_count"] = (
            counter.on_sick_leave
        )  # Считаем количество сотрудников "На больничном"
        context["employee_truancy_count"] = (
            counter.truancy
        )  # Считаем количество сотрудников "Прогул"

        return context


class EmployeeDetailsView(DetailView):
    """Контроллер отображения профиля сотрудников."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_detail.html"


class EmployeeUpdateView(UpdateView):
    """Контроллер обновления профиля сотрудников."""

    model = Employee
    form_class = EmployeeUpdateForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("home_page:home")


class EmployeeDeleteView(DeleteView):
    """Контроллер удаления профиля сотрудников."""

    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("home_page:home")

    def test_func(self):
        return (
            self.request.user.is_staff
        )  # Только суперпользователь может удалять пользователей

    def get_object(self, queryset=None):
        return get_object_or_404(Employee, pk=self.kwargs["pk"])
