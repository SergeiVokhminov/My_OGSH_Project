import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

User = get_user_model()


class Command(BaseCommand):
    """Команда для создания суперпользователя без создания записи в Employee."""

    help = "Создает суперпользователя с генерацией уникального токена"

    def handle(self, *args, **options):
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")

        if not email or not password:
            self.stdout.write(
                self.style.ERROR(
                    "Переменные окружения ADMIN_EMAIL или ADMIN_PASSWORD не заданы"
                )
            )
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f"Пользователь {email} уже существует")
            )
            return

        # 1. Генерируем токен до создания пользователя, чтобы избежать лишних сохранений
        token = None
        while not token:
            candidate = get_random_string(64)
            if not User.objects.filter(token=candidate).exists():
                token = candidate

        # 2. # Создаем объект пользователя напрямую через конструктор модели
        try:
            user = User(
                email=email,
                token=token,
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )
            # Хешируем пароль перед сохранением
            user.set_password(password)
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Суперпользователь создан.\n"
                    f"Логин - {email}\n"
                    f"Пароль - {password}\n"
                    f"Токен - {token}"
                )
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при создании: {e}"))

if __name__ == "__main__":
    pass
