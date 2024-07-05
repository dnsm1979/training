from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise ValidationError("Неверный логин или пароль")
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password_one = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_two = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def clean(self):
        password_one = self.cleaned_data.get("password_one")
        password_two = self.cleaned_data.get("password_two")
        if password_one != password_two:
            raise ValidationError("Пароли не совпадают")
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            raise ValidationError("Такой пользователь уже есть")
        return username


class ChangePasswordForm(forms.Form):

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_one = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_two = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        password_one = self.cleaned_data.get("password_one")
        password_two = self.cleaned_data.get("password_two")
        if password_one != password_two:
            raise ValidationError("Пароли не совпадают")
        return self.cleaned_data

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError("Неверный пароль")
        return old_password
