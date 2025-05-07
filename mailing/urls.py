from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (MessageListView, MessageDetailsView, MessageCreateView,
                           MessageUpdateView, MessageDeleteView, RecipientListView, RecipientDetailsView,
                           RecipientCreateView, RecipientUpdateView, RecipientDeleteView, MessageInfoView,
                           RecipientInfoView)

app_name = MailingConfig.name

urlpatterns = [
    path("message_info/", MessageInfoView.as_view(), name="message_info"),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path("message/create/", MessageCreateView.as_view(), name="message_create"),
    path('message/<int:pk>/', MessageDetailsView.as_view(), name='message_detail'),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),

    path("recipient_info/", RecipientInfoView.as_view(), name="recipient_info"),
    path('recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path("recipient/create/", RecipientCreateView.as_view(), name="recipient_create"),
    path('recipient/<int:pk>/', RecipientDetailsView.as_view(), name='recipient_detail'),
    path("recipient/<int:pk>/update/", RecipientUpdateView.as_view(), name="recipient_update"),
    path("recipient/<int:pk>/delete/", RecipientDeleteView.as_view(), name="recipient_delete"),

]
