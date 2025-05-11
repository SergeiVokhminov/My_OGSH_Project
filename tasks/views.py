from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tasks.forms import TaskUpdateForm
from tasks.models import Task
from tasks.utils import TaskCounter


class TaskInfoView(TemplateView):
    """."""

    model = Task
    form_class = TaskUpdateForm
    template_name = "tasks/tasks_info.html"


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
        counter = TaskCounter()
        context["task_count"] = (
            counter.total()
        )  # Считаем общее количество созданных задач
        context["start_task_count"] = (
            counter.start_task
        )  # Считаем количество задач "К исполнению"
        context["free_task_count"] = (
            counter.free_task
        )  # Считаем количество задач "Свободна"
        context["done_task_count"] = (
            counter.done_task
        )  # Считаем количество задач "Завершена"
        context["closed_task_count"] = (
            counter.closed_task
        )  # Считаем количество задач "Отменена"

        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Task.objects.all()  # Суперпользователь видит все задачи
        else:
            return Task.objects.filter(
                employee=user
            )  # Обычный пользователь видит только свои задачи


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
