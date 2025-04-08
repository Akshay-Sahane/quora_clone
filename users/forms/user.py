from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterViewForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
