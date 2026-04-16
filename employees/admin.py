from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
        "email",
        "last_name",
        "first_name",
        "position",
    )
    list_filter = ("id", "last_name")
    search_fields = ("email", "last_name", "phone_number")
