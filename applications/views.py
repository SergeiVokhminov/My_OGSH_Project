from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from applications.forms import ApplicationUpdateForm
from applications.models import Application


class ApplicationHomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "applications/application_info.html"


class ApplicationCreateView(CreateView):
    """Контроллер создания заявки."""

    model = Application
    form_class = ApplicationUpdateForm
    template_name = "applications/application_form.html"
    success_url = reverse_lazy("applications:application_list")


class ApplicationListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка заявок."""

    model = Application
    context_object_name = "tasks"  # Указываем имя переменной для контекста
    template_name = "applications/application_list.html"
    queryset = Application.objects.all()  # Получение всех задач


class ApplicationDetailsView(DetailView):
    """Контроллер отображения подробностей о заявке."""

    model = Application
    template_name = "applications/application_detail.html"


class ApplicationUpdateView(UpdateView):
    """Контроллер изменения заявки."""

    model = Application
    form_class = ApplicationUpdateForm
    template_name = "applications/application_form.html"
    success_url = reverse_lazy("applications:application_list")


class ApplicationDeleteView(DeleteView):
    """Контроллер удаления заявки."""

    model = Application
    template_name = "applications/application_confirm_delete.html"
    success_url = reverse_lazy("applications:application_list")
