from datetime import datetime

from users.models import User


class UserCounter:
    """Класс для подсчета и работы с количеством пользователей."""

    def __init__(self, queryset=User.objects):
        self.queryset = queryset

    def total(self):
        """Определяем общее количество пользователей."""
        return self.queryset.count()

    def count_by_condition(self, condition):
        """Определяем количество пользователей по статусу сотрудника."""
        return self.queryset.filter(condition=condition).count()

    @property
    def at_work(self):
        """Определяем количество пользователей со статусом 'На работе'."""
        return self.count_by_condition("work")

    @property
    def on_vacation(self):
        """Определяем количество пользователей со статусом 'В отпуске'."""
        return self.count_by_condition("vacation")

    @property
    def on_sick_leave(self):
        """Определяем количество пользователей со статусом 'На больничном'."""
        return self.count_by_condition("sick_leave")

    @property
    def truancy(self):
        """Определяем количество пользователей со статусом 'Прогул'."""
        return self.count_by_condition("truancy")


class TimeGreeting:
    """Класс для вывода приветствия в зависимости от времени."""

    @staticmethod
    def get_greeting():
        """Функция для определения текущего времени и вывода соответствующего приветствия."""

        now = datetime.now()
        hour = now.hour
        if 5 <= hour < 12:
            return "Доброе утро"
        elif 12 <= hour < 18:
            return "Добрый день"
        elif 18 <= hour < 23:
            return "Добрый вечер"
        else:
            return "Доброй ночи"
