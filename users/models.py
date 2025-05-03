from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Поля для модели пользователя."""

    at_work = "work"
    on_vacation = "vacation"
    on_sick_leave = "sick_leave"
    truancy = "truancy"

    CONDITION_CHOICES = [
        (at_work, "На работе"),
        (on_vacation, "В отпуске"),
        (on_sick_leave, "На больничном"),
        (truancy, "Прогул")
    ]

    username = None
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
    phone_number = models.CharField(
        max_length=25, verbose_name="Номер телефона", blank=True, null=True
    )
    position = models.CharField(
        max_length=100, verbose_name="Должность", blank=True, null=True
    )
    condition = models.CharField(
       choices=CONDITION_CHOICES,
       verbose_name="Статус сотрудника",
       default="truancy",
       null=True,
       blank=True,
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
        max_length=100, verbose_name="Токен пользователя", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.last_name} {self.first_name}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
