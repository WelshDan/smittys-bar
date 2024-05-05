from django import forms
from django.forms import ModelForm
from .models import CustomUser


class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'start_date', 'is_active', 'is_superuser']
