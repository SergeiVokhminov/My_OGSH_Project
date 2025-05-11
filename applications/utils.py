from applications.models import Application


class ApplicationCounter:
    """Класс для подсчета и работы с количеством задач."""

    def __init__(self, queryset=Application.objects):
        self.queryset = queryset

    def total(self):
        """Определяем общее количество созданных заявок."""
        return self.queryset.count()
