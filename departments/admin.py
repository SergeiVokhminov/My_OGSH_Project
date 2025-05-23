from django.contrib import admin

from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "number_of_people"
    )
    list_filter = ("name",)
    search_fields = ("name",)
