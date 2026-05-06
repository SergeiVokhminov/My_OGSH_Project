import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Поля для модели пользователя."""

    username = None  # отключаем использование поля username
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта"
    )  # почта уникальна
    token = models.CharField(
        max_length=64,
        verbose_name="Токен пользователя",
        unique=True,
        editable=False,
        blank=True,
        null=True,
    )  # секретный токен

    USERNAME_FIELD = "email"  # используем почту, как основное поле (обязательное для ввода)
    REQUIRED_FIELDS = []  # можно добавить дополнительные поля

    #  генерация секретного токена
    def save(self, *args, **kwargs):
        """Переопределение метода сохранения для генерации токена при создании."""

        if not self.token:
            self.token = secrets.token_urlsafe(32)
        super().save(*args, **kwargs)

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.email}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Зарегистрированный пользователь"
        verbose_name_plural = "Зарегистрированные пользователи"
        ordering = ["id"]
