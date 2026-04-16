from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home_page.urls"), name="home_page"),
    path("users/", include("users.urls"), name="user"),
    path("tasks/", include("tasks.urls"), name="task"),
    path("employees/", include("employees.urls"), name="employee"),
    path("departments/", include("departments.urls"), name="department"),
    path("blogs/", include("blogs.urls"), name="blog"),
    path("applications/", include("applications.urls"), name="application"),
    # path("mailing/", include("mailing.urls"), name="mailing"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
