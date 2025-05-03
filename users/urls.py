from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    HomeView,
    UserDeleteView,
    UserDetailsView,
    UserInfoView,
    UserListView,
    UserRegisterView,
    UserUpdateView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="users:home"), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("user/info/<int:pk>/", UserInfoView.as_view(), name="user_info"),
    path("user/list/", UserListView.as_view(), name="user_list"),
    path("user/detail/<int:pk>/", UserDetailsView.as_view(), name="user_detail"),
    path("user/update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
