from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
        "email",
        "date_joined",
        "is_active",
    )
    list_filter = ("id",)
    search_fields = ("email",)
