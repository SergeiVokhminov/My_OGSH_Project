from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
        "email",
        "last_name",
        "first_name",
        "last_login",
        "is_active",
    )
    list_filter = ("id", "last_name")
    search_fields = ("email", "last_name", "phone_number")
