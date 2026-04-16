from users.models import User


class UserCounter:
    """Класс для подсчета и работы с количеством зарегистрированных пользователей."""

    def __init__(self, queryset=User.objects):
        self.queryset = queryset

    def total(self):
        """Определяем общее количество зарегистрированных пользователей."""

        return self.queryset.count()
