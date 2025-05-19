from django.db import models


class Application(models.Model):
    """Поля для модели заявки."""

    DEPARTMENT_CHOICES = [
        ("OGESh", "ОЭГШ"),
        ("SB", "CБ"),
        ("SIT", "СИТ"),
        ("OGM", "ОГМ"),
        # Добавить другие отделы при необходимости
    ]
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        verbose_name="Отдел"
    )
    title = models.CharField(
        max_length=250,
        verbose_name="Название заявки",
    )
    description = models.TextField(
        verbose_name="Описание заявки",
        null=True,
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
