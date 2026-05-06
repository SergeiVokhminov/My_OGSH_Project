import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from transliterate import translit

from employees.constants import CONDITION_CHOICES


class Employee(models.Model):
    """Поля для модели профиля пользователя."""

    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    first_name = models.CharField(
        max_length=50, verbose_name="Имя", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Фамилия"
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
    avatar = models.ImageField(
        upload_to="photo/avatars/", verbose_name="Аватар", blank=True, null=True
    )
    last_login = models.DateTimeField(auto_now=True, verbose_name="Последний вход")
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )
    token = models.CharField(
        max_length=64,
        verbose_name="Токен пользователя",
        unique=True,
        editable=False,
        blank=True,
        null=True,
    )  # секретный токен
    password = models.CharField(max_length=128, verbose_name="Пароль", blank=True, null=True)  # хранится в зашифрованном виде
    condition = models.CharField(
        choices=CONDITION_CHOICES,
        verbose_name="Статус сотрудника",
        default="work",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def save(self, *args, **kwargs):
        """Переопределение метода сохранения для генерации токена при создании."""

        if not self.token:
            self.token = uuid.uuid4().hex

        # Проверяем, если пароль еще не хэширован, хэшируем его.
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)

        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        """Метод для установки пароля, хэширует его."""

        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Метод проверки пароля."""

        return check_password(raw_password, self.password)

    def get_email(self):
        """ Генерирует email исходя из фамилии и шаблона. """

        # Получаем значение фамилии
        last_name = self.last_name  # Это значение, а не само поле

        # Переводим фамилию с русского на английский.
        last_name_transliterated = translit(last_name, 'ru', reversed=True).lower()

        return f"{last_name_transliterated}@test_pr.ru"

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.last_name} {self.first_name} - {self.email}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
        ordering = ["id"]
