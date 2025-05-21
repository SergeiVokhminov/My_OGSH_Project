from django.db import models


class Department(models.Model):
    """Поля для модели отдел."""

    name = models.CharField(
        max_length=50,
        verbose_name="Название Отдела"
    )
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", null=True, blank=True)
    number_of_people = models.IntegerField(verbose_name="Количество сотрудников", null=True, blank=True)

    def __str__(self):
        """Метод для строкового представления объекта Department."""

        return f"{self.name}"

    class Meta:
        """Мета-информация модели Department."""

        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
