from django.urls import path

from applications.apps import ApplicationsConfig
from applications.views import (ApplicationCreateView, ApplicationDeleteView,
                                ApplicationDetailsView, ApplicationHomeView,
                                ApplicationListView, ApplicationUpdateView)

app_name = ApplicationsConfig.name

urlpatterns = [
    path("info/", ApplicationHomeView.as_view(), name="application_info"),
    path("create/", ApplicationCreateView.as_view(), name="application_create"),
    path("list/", ApplicationListView.as_view(), name="application_list"),
    path(
        "detail/<int:pk>/", ApplicationDetailsView.as_view(), name="application_detail"
    ),
    path(
        "update/<int:pk>/", ApplicationUpdateView.as_view(), name="application_update"
    ),
    path(
        "delete/<int:pk>/", ApplicationDeleteView.as_view(), name="application_delete"
    ),
]
