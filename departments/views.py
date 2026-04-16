from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from departments.forms import DepartmentUpdateForm
from departments.models import Department


class DepartmentInfoView(TemplateView):
    """Контроллер страницы о задачах."""

    model = Department
    form_class = DepartmentUpdateForm
    template_name = "tasks/tasks_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class DepartmentCreateView(CreateView):
    """Контроллер создания задачи."""

    model = Department
    form_class = DepartmentUpdateForm
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("departments:department_list")

    def form_valid(self, form):
        department = form.save()
        user = self.request.user
        department.owner = user
        department.save()
        return super().form_valid(form)

    def test_func(self):
        """Проверка, является ли пользователь суперпользователем."""

        return self.request.user.is_superuser


class DepartmentListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка задач."""

    model = Department
    context_object_name = "departments"  # Указываем имя переменной для контекста
    template_name = "departments/department_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Department.objects.all()  # Суперпользователь видит все задачи
        else:
            return Department.objects.filter(
                employee=user
            )  # Обычный пользователь видит только свои задачи


class DepartmentDetailsView(DetailView):
    """Контроллер отображения подробностей о задаче."""

    model = Department
    template_name = "departments/department_detail.html"


class DepartmentUpdateView(UpdateView):
    """Контроллер изменения задачи."""

    model = Department
    form_class = DepartmentUpdateForm
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("departments:department_list")


class DepartmentDeleteView(DeleteView):
    """Контроллер удаления задачи."""

    model = Department
    template_name = "departments/department_confirm_delete.html"
    success_url = reverse_lazy("departments:department_list")
