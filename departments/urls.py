from django.urls import path

from departments.apps import DepartmentsConfig
from departments.views import (
    DepartmentListView,
    DepartmentInfoView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDetailsView,
    DepartmentDeleteView,
)

app_name = DepartmentsConfig.name

urlpatterns = [
    path("info", DepartmentInfoView.as_view(), name="department_info"),
    path("create/", DepartmentCreateView.as_view(), name="department_create"),
    path("list/", DepartmentListView.as_view(), name="department_list"),
    path("detail/<int:pk>/", DepartmentDetailsView.as_view(), name="department_detail"),
    path("update/<int:pk>/", DepartmentUpdateView.as_view(), name="department_update"),
    path("delete/<int:pk>/", DepartmentDeleteView.as_view(), name="department_delete"),
]
