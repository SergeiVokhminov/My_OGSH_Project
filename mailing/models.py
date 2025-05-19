from django.db import models


class Message(models.Model):
    """Поля для модели сообщения."""

    topic = models.CharField(max_length=100, verbose_name="Тема сообщения")
    text = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        """Метод для строкового представления объекта Message."""

        return self.topic

    class Meta:
        """Мета-информация модели Message."""

        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]


class Recipient(models.Model):
    """Поля для модели получателя рассылки."""

    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    first_name = models.CharField(max_length=250, verbose_name="Имя получателя")
    last_name = models.CharField(max_length=250, verbose_name="Фамилия получателя")
    patronymic = models.CharField(
        max_length=250,
        verbose_name="Отчество получателя",
        null=True,
        blank=True,
    )
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)

    def __str__(self):
        """Метод для строкового представления объекта Recipient."""

        return f"{self.first_name}.{self.last_name} - {self.email}"

    class Meta:
        """Мета-информация модели Recipient."""

        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
