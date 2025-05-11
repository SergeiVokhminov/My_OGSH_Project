from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import (
    TaskCreateView,
    TaskDetailsView,
    TaskListView,
    TasksDeleteView,
    TaskUpdateView, TaskInfoView,
)

app_name = TasksConfig.name

urlpatterns = [
    path("info", TaskInfoView.as_view(), name="task_info"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("list/", TaskListView.as_view(), name="task_list"),
    path("detail/<int:pk>/", TaskDetailsView.as_view(), name="task_detail"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TasksDeleteView.as_view(), name="task_delete"),
]
