from tasks.models import Task


class TaskCounter:
    """Класс для подсчета и работы с количеством задач."""

    def __init__(self, queryset=Task.objects):
        self.queryset = queryset

    def total(self):
        """Определяем общее количество созданных задач."""
        return self.queryset.count()

    def count_by_status(self, status):
        """Определение количества задач по статусу."""
        return self.queryset.filter(status=status).count()

    @property
    def start_task(self):
        """Определение количества задач по статусу 'К исполнению'."""
        return self.count_by_status("start")

    @property
    def free_task(self):
        """Определение количества задач по статусу 'Свободна'."""
        return self.count_by_status("free")

    @property
    def done_task(self):
        """Определение количества задач по статусу 'Выполнена'."""
        return self.count_by_status("done")

    @property
    def closed_task(self):
        """Определение количества задач по статусу 'Отменена'."""
        return self.count_by_status("closed")
