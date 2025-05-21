from django.db import models

from departments.models import Department


class Application(models.Model):
    """Поля для модели заявки."""

    title = models.CharField(
        max_length=250,
        verbose_name="Название заявки",
    )
    description = models.TextField(
        verbose_name="Описание заявки",
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Отдел",
        related_name="departments",
        default="Не выбран",
        blank=True,
    )
    deadline = models.DateField(
        verbose_name="Дата исполнения",
        null=True,
        blank=True,
    )
    times = models.TimeField(
        verbose_name="Время исполнения",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        """Метод для строкового представления объекта Application."""

        return f"{self.title}"

    class Meta:
        """Мета-информация модели Application."""

        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
