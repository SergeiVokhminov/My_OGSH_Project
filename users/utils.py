from users.models import User


class UserCounter:
    """Класс для подсчета и работы с количеством зарегистрированных пользователей."""

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
