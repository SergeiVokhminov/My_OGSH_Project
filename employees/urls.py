from django.urls import path

from employees.apps import EmployeesConfig
from employees.views import (
    EmployeeCreateView,
    EmployeeDeleteView,
    EmployeeDetailsView,
    EmployeeInfoView,
    EmployeeListView,
    EmployeeUpdateView,
)

app_name = EmployeesConfig.name

urlpatterns = [
    path("list/", EmployeeListView.as_view(), name="employee_list"),
    path("create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("info/<int:pk>/", EmployeeInfoView.as_view(), name="employee_info"),
    path("detail/<int:pk>/", EmployeeDetailsView.as_view(), name="employee_detail"),
    path("update/<int:pk>/", EmployeeUpdateView.as_view(), name="employee_update"),
    path("delete/<int:pk>/", EmployeeDeleteView.as_view(), name="employee_delete"),
]
