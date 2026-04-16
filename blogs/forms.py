from django import forms
from blogs.models import Blog
from users.models import User


class BlogForm(forms.ModelForm):
    """Форма для представления блога."""

    class Meta:
        model = Blog
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
