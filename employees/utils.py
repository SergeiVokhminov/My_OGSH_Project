from employees.models import Employee


class EmployeeCounter:
    """Класс для подсчета и работы с количеством сотрудников."""

    def __init__(self, queryset=Employee.objects):
        self.queryset = queryset

    def total(self):
        """Определяем общее количество сотрудников."""
        return self.queryset.count()

    def count_by_condition(self, condition):
        """Определяем количество сотрудников по статусу."""
        return self.queryset.filter(condition=condition).count()

    @property
    def at_work(self):
        """Определяем количество сотрудников со статусом 'На работе'."""
        return self.count_by_condition("work")

    @property
    def on_vacation(self):
        """Определяем количество сотрудников со статусом 'В отпуске'."""
        return self.count_by_condition("vacation")

    @property
    def on_sick_leave(self):
        """Определяем количество сотрудников со статусом 'На больничном'."""
        return self.count_by_condition("sick_leave")

    @property
    def truancy(self):
        """Определяем количество сотрудников со статусом 'Прогул'."""
        return self.count_by_condition("truancy")
