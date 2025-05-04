# from datetime import datetime
#
# from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.http import HttpResponseForbidden
from django.db.models import Count, Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from requests import Response

from tasks.forms import TaskUpdateForm
from tasks.models import Task


class TaskCreateView(CreateView):
    """Контроллер создания задачи."""

    model = Task
    form_class = TaskUpdateForm
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:task_list")

    def form_valid(self, form):
        task = form.save()
        user = self.request.user
        task.owner = user
        task.save()
        return super().form_valid(form)

    def test_func(self):
        """Проверка, является ли пользователь суперпользователем."""

        return self.request.user.is_superuser


class TaskListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка задач."""

    model = Task
    context_object_name = "tasks"  # Указываем имя переменной для контекста
    template_name = "tasks/tasks_list.html"
    queryset = Task.objects.all()  # Получение всех задач

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_count"] = Task.objects.count()  # Считаем общее количество созданных задач
        context["start_task_count"] = Task.objects.filter(
            status="start"
        ).count()  # Считаем количество задач "К исполнению"
        context["free_task_count"] = Task.objects.filter(status="free").count()  # Считаем количество задач "Свободна"
        context["done_task_count"] = Task.objects.filter(status="done").count()  # Считаем количество задач "Завершена"
        context["closed_task_count"] = Task.objects.filter(
            status="closed"
        ).count()  # Считаем количество задач "Отменена"

        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Task.objects.all()  # Суперпользователь видит все задачи
        else:
            return Task.objects.filter(employee=user)  # Обычный пользователь видит только свои задачи


class TaskDetailsView(DetailView):
    """Контроллер отображения подробностей о задаче."""

    model = Task
    template_name = "tasks/tasks_detail.html"


class TaskUpdateView(UpdateView):
    """Контроллер изменения задачи."""

    model = Task
    form_class = TaskUpdateForm
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:task_list")


class TasksDeleteView(DeleteView):
    """Контроллер удаления задачи."""

    model = Task
    template_name = "tasks/tasks_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_list")
