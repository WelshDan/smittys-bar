from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserAdminConfig(UserAdmin):

    model = CustomUser
    
    search_fields = ('email', 'user_id',)
    list_filter = ('email', 'user_id', 'is_active', 'is_superuser',)
    ordering = ('-user_id',)
    list_display = ('email', 'user_id', 'is_active', 'is_superuser',)

    fieldsets = (
        (None, { 'fields': ('email',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    )


admin.site.register(CustomUser, UserAdminConfig)
