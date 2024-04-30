from django import forms
from django.forms import ModelForm
from .models import CustomUser


class RegisterForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
