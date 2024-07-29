# forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')

        if not first_name and not last_name:
            raise ValidationError("Хотя бы одно из полей 'first_name' или 'last_name' должно быть заполнено.")
        if not email:
            raise ValidationError("Поле 'email' обязательно для заполнения.")
        return cleaned_data
