from django import forms

from applications.models import Application


class ApplicationUpdateForm(forms.ModelForm):
    """Форма для задачи."""

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
            {"class": "form-control", "placeholder": "Введите срок исполнения заявки"}
        )


class ConfirmTaskForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Я подтверждаю выполнение задачи")
