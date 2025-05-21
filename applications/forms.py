from django import forms

from applications.models import Application


class ApplicationUpdateForm(forms.ModelForm):
    """Форма для обновления заявки."""

    class Meta:
        model = Application
        fields = (
            "title",
            "description",
            "department",
            "deadline",
            "times"
        )
        widgets = {
            "deadline": forms.SelectDateWidget(),
            "times": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationUpdateForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Введите название заявки"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Введите описание заявки"}
        )
        self.fields["department"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Выберите Отдел"}
        )
        self.fields["deadline"].widget.attrs.update(
            {"class": "form-control mb-3"}
        )
        self.fields["times"].widget.attrs.update(
            {"class": "form-control mb-3"}
        )
