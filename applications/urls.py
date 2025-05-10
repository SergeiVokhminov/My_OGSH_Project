from django.urls import path

from applications.apps import ApplicationsConfig
from applications.views import (
    ApplicationHomeView,
    ApplicationCreateView,
    ApplicationListView,
    ApplicationDeleteView,
    ApplicationUpdateView,
    ApplicationDetailsView,

    # проверка новых представлений
    NewApplicationCreateView
)

app_name = ApplicationsConfig.name

urlpatterns = [
    path("info/", ApplicationHomeView.as_view(), name="application_info"),
    path("create/", ApplicationCreateView.as_view(), name="application_create"),
    path("list/", ApplicationListView.as_view(), name="application_list"),
    path("detail/<int:pk>/", ApplicationDetailsView.as_view(), name="application_detail"),
    path("update/<int:pk>/", ApplicationUpdateView.as_view(), name="application_update"),
    path("delete/<int:pk>/", ApplicationDeleteView.as_view(), name="application_delete"),

    # проверка новых маршрутов
    path("new_form/", NewApplicationCreateView.as_view(), name="new_application_form"),
]
