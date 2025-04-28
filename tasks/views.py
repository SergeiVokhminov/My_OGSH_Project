# from datetime import datetime
#
# from django.conf import settings
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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


class TaskListView(ListView):
    """Контроллер отображения списка задач."""

    model = Task
    context_object_name = "tasks"  # Указываем имя переменной для контекста
    template_name = "tasks/tasks_list.html"
    queryset = Task.objects.all()  # Получение всех задач

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_count"] = Task.objects.count() # Считаем количество пользователей

        return context


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
