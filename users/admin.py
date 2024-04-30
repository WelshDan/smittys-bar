from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'user_id',)
    list_filter = ('email', 'user_id', 'start_date', 'is_active', 'is_superuser',)
    ordering = ('-user_id',)
    list_display = ('email', 'user_id', 'start_date', 'is_active', 'is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'user_id', 'start_date',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'user_id', 'start_date', 'is_active', 'is_superuser',)}
        ),
    )

admin.site.register(CustomUser, UserAdminConfig)
