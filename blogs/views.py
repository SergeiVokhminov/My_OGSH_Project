from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogInfoView(TemplateView):
    """Контроллер страницы о блогах."""

    model = Blog
    form_class = BlogForm
    template_name = "blogs/blog_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BlogCreateView(CreateView):
    """Контроллер создания блога."""

    model = Blog
    form_class = BlogForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blogs:blog_list")

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)

    def test_func(self):
        """Проверка, является ли пользователь суперпользователем."""

        return self.request.user.is_superuser


class BlogListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка блогов."""

    model = Blog
    context_object_name = "blogs"  # Указываем имя переменной для контекста
    template_name = "blogs/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Blog.objects.all()  # Суперпользователь видит все блоги
        else:
            return Blog.objects.filter(
                employee=user
            )  # Обычный пользователь видит только свои блоги


class BlogDetailsView(DetailView):
    """Контроллер отображения подробностей о блоге."""

    model = Blog
    template_name = "blogs/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Контроллер изменения блога."""

    model = Blog
    form_class = BlogForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    """Контроллер удаления блога."""

    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blogs:blog_list")
