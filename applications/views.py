from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from applications.forms import ApplicationUpdateForm
from applications.models import Application
from applications.utils import ApplicationCounter


class ApplicationHomeView(TemplateView):
    """Контроллер представления главной страницы заявок."""

    template_name = "applications/application_info.html"


class ApplicationCreateView(CreateView):
    """Контроллер создания заявки."""

    model = Application
    form_class = ApplicationUpdateForm
    template_name = "applications/application_form.html"
    success_url = reverse_lazy("applications:application_list")


class ApplicationListView(ListView):
    """Контроллер отображения списка заявок."""

    model = Application
    template_name = "applications/application_list.html"
    queryset = Application.objects.all()  # Получение всех заявок

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter_application = ApplicationCounter()
        context["application_count"] = (
            counter_application.total()
        )  # Считаем количество заявок

        return context


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
