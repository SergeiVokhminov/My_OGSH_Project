from django.urls import path

from home_page.apps import HomePageConfig
from home_page.views import (
    HomeView,
)

app_name = HomePageConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
