from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        readonly_fields = ['id']
        fields = ['email','password', 'start_date', 'is_active', 'is_superuser']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        readonly_fields = ['id']
        fields = ['email','password', 'start_date', 'is_active', 'is_superuser']
