from datetime import datetime

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Контроллер создания задачи."""

    model = Task
    form_class = TaskForm
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:task_list")

    def test_func(self):
        """Проверка, является ли пользователь суперпользователем."""

        return self.request.user.is_superuser


class TaskListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка задач."""

    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"  # Указываем имя переменной для контекста
    queryset = Task.objects.all()  # Получение всех задач


class TaskDetailsView(LoginRequiredMixin, DetailView):
    """Контроллер отображения подробностей о задаче."""

    model = Task
    template_name = "tasks/tasks_detail.html"


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Контроллер изменения задачи."""

    model = Task
    form_class = TaskForm
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:task_list")

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user != task.owner:
            return HttpResponseForbidden("У вас нет прав для редактирования продукта.")

    def test_func(self):
        recipient = self.get_object()
        return self.request.user == recipient.owner

    def handle_no_permissions(self):
        return HttpResponseForbidden("У вас нет прав на это действие.")

    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.pk})


class TasksDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер удаления задачи."""

    model = Task
    template_name = "tasks/tasks_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_list")

    def test_func(self):
        recipient = self.get_object()
        return self.request.user == recipient.owner

    def handle_no_permissions(self):
        return HttpResponseForbidden("У вас нет прав на это действие.")
