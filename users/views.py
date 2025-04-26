from django.views.generic import TemplateView

from users.models import User


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "users/home.html"
