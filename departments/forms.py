from django import forms

from departments.models import Department
from users.models import User


class DepartmentForm(forms.ModelForm):
    """Форма для задачи."""

    class Meta:
        model = Department
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)


class DepartmentUpdateForm(forms.ModelForm):
    """Форма для обновления задачи."""

    class Meta:
        model = Department
        fields = (
            "name",
            "phone",
            "number_of_people",
        )
        widgets = {
            "deadline": forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentUpdateForm, self).__init__(*args, **kwargs)
        self.fields["employee"].queryset = User.objects.exclude(is_superuser=True)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название Отдела"}
        )
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите номер телефона Отдела"}
        )
        self.fields["number_of_people"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Выберите количество работников Отдела",
            }
        )
