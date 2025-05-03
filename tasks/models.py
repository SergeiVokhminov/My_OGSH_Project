from django.db import models

from config import settings
from users.models import User


class Task(models.Model):
    """Поля для модели задача."""

    START_STATUS = "start"
    DONE_STATUS = "done"
    FREE_STATUS = "free"
    CLOSED_STATUS = "closed"

    STATUS_CHOICES = [
        (START_STATUS, "К исполнению"),
        (DONE_STATUS, "Выполнена"),
        (FREE_STATUS, "Свободна"),
        (CLOSED_STATUS, "Отменена"),
    ]

    title = models.CharField(
        max_length=250,
        verbose_name="Название задачи",
    )
    description = models.TextField(
        verbose_name="Описание задачи",
        null=True,
        blank=True,
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="subtask",
        verbose_name="Родительская задача",
        null=True,
        blank=True,
    )
    employee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="tasks",
        verbose_name="Исполнители",
        default="Не выбран",
        blank=True,
        null=True,
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        verbose_name="Статус",
        default="free",
        null=True,
        blank=True,
    )
    deadline = models.DateField(
        verbose_name="Строк исполнения",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(
        default=False, verbose_name="Признак активной задачи"
    )
    is_related = models.BooleanField(
        default=False, verbose_name="Признак связанной задачи"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец задачи",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
