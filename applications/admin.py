from django.contrib import admin

from applications.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "deadline",
        "created_at",
        "updated_at",
    )
    list_filter = ("title", "deadline")
    search_fields = ("title",)
