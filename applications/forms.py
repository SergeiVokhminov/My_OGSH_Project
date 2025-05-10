from django import forms

from applications.models import Application


class ApplicationForm(forms.ModelForm):
    """Форма для задачи."""

    class Meta:
        model = Application
        exclude = ("title", "description", "deadline", "times")

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)


class ApplicationUpdateForm(forms.ModelForm):
    """Форма для обновления заявки."""

    class Meta:
        model = Application
        fields = (
            "title",
            "description",
            "deadline",
        )

    def __init__(self, *args, **kwargs):
        super(ApplicationUpdateForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название заявки"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание заявки"}
        )
        self.fields["deadline"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите срок исполнения заявки в формате 00.00.0000"}
        )


class ConfirmTaskForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Я подтверждаю выполнение задачи")
