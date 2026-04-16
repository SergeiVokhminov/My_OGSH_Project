from django.contrib import admin

from tasks.models import Task
from users.models import User


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Настройки отображения модели Task в админ-панели Django."""

    list_display = ("id", "title", "status", "deadline")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Исключаем администратора из списка исполнителей
        if db_field.name == "employee":
            kwargs["queryset"] = User.objects.exclude(is_superuser=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
