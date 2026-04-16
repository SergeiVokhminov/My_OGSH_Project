from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "image",
        "created_at",
        "updated_at",
        "publication_sign",
        "views",
    )
    list_filter = ("title",)
    search_fields = ("title",)
