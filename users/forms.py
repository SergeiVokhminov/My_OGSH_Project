from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)

from users.models import User
from users.validators import validate_email_address, validate_phone_number


class UserForm(forms.ModelForm):
    """Форма представления пользователя."""

    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)


class UserAuthForm(AuthenticationForm):
    """Форма входа на сайт."""

    pass


class UserRegisterForm(UserCreationForm):
    """Форма регистрации пользователя на сайте."""

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )

    def clean_email(self):
        """Проверка электронной почты."""

        email_address = self.cleaned_data.get("email")
        return validate_email_address(email_address, self.instance)


class UserUpdateForm(forms.ModelForm):
    """Форма обновления данных."""

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "position",
            "phone_number",
            "condition",
            "address",
            "avatar",
        )

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите фамилию"}
        )
        self.fields["patronymic"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите отчество"}
        )
        self.fields["position"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите должность"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите номер телефона (только цифры)",
            }
        )
        self.fields["condition"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите статус сотрудника"}
        )
        self.fields["address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес регистрации"}
        )
        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите фотографию"}
        )

    def clean_email(self):
        """Проверка электронной почты."""

        email_address = self.cleaned_data.get("email")
        return validate_email_address(email_address, self.instance)

    def clean_phone_number(self):
        """Проверка телефонного номера."""

        phone_number = self.cleaned_data.get("phone_number")
        return validate_phone_number(phone_number)
