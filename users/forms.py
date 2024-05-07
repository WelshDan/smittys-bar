from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import User
from .models import User


class RegisterForm(ModelForm):

    class Meta:

        model = User
        fields = ['email','password', 'date_joined', 'is_active', 'is_superuser']

