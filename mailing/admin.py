from django.contrib import admin

from mailing.models import Recipient, Message


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "patronymic", "comment")
    search_fields = ("email", "last_name")
    list_filter = ("email", "last_name")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "text")
    search_fields = ("topic",)
    list_filter = ("topic",)
