from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import (
    BlogInfoView,
    BlogCreateView,
    BlogListView,
    BlogDetailsView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogsConfig.name

urlpatterns = [
    path("info", BlogInfoView.as_view(), name="blog_info"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("list/", BlogListView.as_view(), name="blog_list"),
    path("detail/<int:pk>/", BlogDetailsView.as_view(), name="blog_detail"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
]
