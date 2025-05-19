from django.db import models


class Department(models.Model):
    """Поля для модели отдела."""

    DEPARTMENT_CHOICES = [
        ("OGESh", "ОЭГШ"),
        ("SB", "CБ"),
        ("SIT", "СИТ"),
        ("OGM", "ОГМ"),
        # Добавить другие отделы при необходимости
    ]
    name = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        verbose_name="Название Отдела"
    )

    def __str__(self):
        """Метод для строкового представления объекта Department."""

        return f"{self.name}"

    class Meta:
        """Мета-информация модели Department."""

        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
