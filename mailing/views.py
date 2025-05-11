from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from mailing.forms import MessageForm, RecipientForm
from mailing.models import Message, Recipient


class HomeView(TemplateView):
    template_name = "mailing/home.html"


class MessageInfoView(TemplateView):
    template_name = "mailing/message_info.html"


class RecipientInfoView(TemplateView):
    template_name = "mailing/recipient_info.html"


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка сообщений."""

    model = Message
    template_name = "mailing/message_list.html"


class MessageDetailsView(LoginRequiredMixin, DetailView):
    """Контроллер отображения подробностей о сообщении."""

    model = Message
    template_name = "mailing/message_detail.html"


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания сообщения."""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message_form.html"
    success_url = reverse_lazy("mailing:message_list")

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Контроллер изменения сообщения."""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер удаления сообщения."""

    model = Message
    template_name = "mailing/message_confirm_delete.html"
    success_url = reverse_lazy("mailing:message_list")


class RecipientListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка получателей."""

    model = Recipient
    template_name = "mailing/recipient_list.html"


class RecipientDetailsView(LoginRequiredMixin, DetailView):
    """Контроллер отображения подробностей о получателе."""

    model = Recipient
    template_name = "mailing/recipient_detail.html"


class RecipientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания получателя."""

    model = Recipient
    form_class = RecipientForm
    template_name = "mailing/recipient_form.html"
    success_url = reverse_lazy("mailing:recipient_list")

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Контроллер изменения получателя."""

    model = Recipient
    form_class = RecipientForm
    template_name = "mailing/recipient_form.html"
    success_url = reverse_lazy("mailing:recipient_list")


class RecipientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер удаления получателя."""

    model = Recipient
    template_name = "mailing/recipient_confirm_delete.html"
    success_url = reverse_lazy("mailing:recipient_list")
