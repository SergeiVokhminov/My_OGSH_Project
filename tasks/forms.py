from django import forms

from tasks.models import Task
from users.models import User


class TaskForm(forms.ModelForm):
    """Форма для задачи."""

    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["employee"].queryset = User.objects.exclude(is_superuser=True)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название задачи"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание задачи"}
        )
        self.fields["parent_task"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите родительскую задачу"}
        )
        self.fields["employee"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите исполнителя"}
        )
        self.fields["status"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Статус задачи"}
        )
        self.fields["deadline"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите срок исполнения"}
        )
        self.fields["owner"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Создатель задачи"}
        )
