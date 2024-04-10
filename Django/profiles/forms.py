from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.validators import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=2, label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, min_length=2, label="Заголовок", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)



    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            raise ValidationError("Неверный логин или пароль")
        return self.cleaned_data



class RegistrForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=2, label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, min_length=2, label="Пароль-1", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=100, min_length=2, label="Пароль-2",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError("Пароли не совпадают")
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        User = get_user_model()
        if get_user_model().objects.filter(username=username).exists():
            raise ValidationError("Такой пользователь уже есть!")
        return username

class SetPasswordForm(forms.Form):

    password_old = forms.CharField(max_length=100, min_length=2, label="Старый пароль",
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_new = forms.CharField(max_length=100, min_length=2, label="Новый пароль",
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_re = forms.CharField(max_length=100, min_length=2, label="Повторите новый пароль",
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        password_old = self.cleaned_data.get('password_old')
        password_new = self.cleaned_data.get('password_new')
        password_re = self.cleaned_data.get('password_re')
        if password_re != password_new:
            raise ValidationError("Пароли не совпадают")
        return self.cleaned_data

    # def __init__(self, request=None, *args, **kwargs):
    #     self.request = request
    #     super().__init__(*args, **kwargs)
    #
    #
    #
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     user = authenticate(self.request, username=username, password=password)
    #     if user is None:
    #         raise ValidationError("Неверный логин или пароль")
    #     return self.cleaned_data

