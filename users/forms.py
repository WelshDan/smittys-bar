from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import CustomUser
from .models import Customers


class RegisterForm(ModelForm):

    class Meta:
        model = Customers
        fields = ['email', 'password']
