import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.ru'})
    )

    phone_number = forms.CharField(
        label="Номер телефона",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '+7 (900) 123-45-67'})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'email': 'Email',
            'phone_number': 'Номер телефона',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите логин'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль (не менее 8 символов)'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        digits = re.sub(r'[^\d]+', '', phone)
        if len(digits) < 10:
            raise forms.ValidationError("Номер слишком короткий")
        return '+7' + digits[-10:]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин или Номер телефона",
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин или +7...'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )