import uuid

from django.conf import settings
from django.db import models

from employees.constants import CONDITION_CHOICES


class Employee(models.Model):
    """Поля для модели профиля пользователя."""

    condition = models.CharField(
        choices=CONDITION_CHOICES,
        verbose_name="Статус сотрудника",
        default="work",
        null=True,
        blank=True,
    )
    user_account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employee_profile",
        verbose_name="профиль сотрудника",
    )
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    first_name = models.CharField(
        max_length=50, verbose_name="Имя", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Фамилия", blank=True, null=True
    )
    patronymic = models.CharField(
        max_length=50, verbose_name="Отчество", blank=True, null=True
    )
    position = models.CharField(
        max_length=100, verbose_name="Должность", blank=True, null=True
    )
    department = models.CharField(
        max_length=50,
        verbose_name="Структурное подразделение",
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=25, verbose_name="Номер телефона", blank=True, null=True
    )
    address = models.CharField(
        max_length=255, verbose_name="Адрес", blank=True, null=True
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True
    )
    last_login = models.DateTimeField(auto_now=True, verbose_name="Последний вход")
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )
    avatar = models.ImageField(
        upload_to="photo/avatars/", verbose_name="Аватар", blank=True, null=True
    )
    token = models.CharField(
        max_length=100, verbose_name="Токен пользователя", unique=True, editable=False
    )
    is_active = models.BooleanField(default=True, verbose_name="Признак активности")

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.last_name} {self.first_name} - {self.position}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
