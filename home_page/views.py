from django.views.generic import (
    TemplateView,
)

# from applications.utils import ApplicationCounter
# from employees.utils import EmployeeCounter
# from tasks.utils import TaskCounter
from home_page.utils import TimeGreeting


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "home_page/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # counter_employee = EmployeeCounter()
        # counter_task = TaskCounter()
        # counter_application = ApplicationCounter()
        context["greeting"] = TimeGreeting.get_greeting()  # Применяем класс приветствия
        # context["employee_at_work_count"] = (
        #     counter_employee.at_work
        # )  # Считаем количество пользователей "На работе"
        # context["start_task_count"] = (
        #     counter_task.start_task
        # )  # Считаем количество задач "К исполнению"
        # context["free_task_count"] = (
        #     counter_task.free_task
        # )  # Считаем количество задач "Свободна" application_count
        # context["application_count"] = (
        #     counter_application.total # Считаем общее количество заявок
        # )
        return context
