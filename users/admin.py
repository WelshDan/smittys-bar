from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'id',)
    list_filter = ('email', 'id', 'start_date', 'is_active', 'is_superuser',)
    ordering = ('-id',)
    list_display = ('email', 'id', 'start_date', 'is_active', 'is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'id', 'start_date',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'id', 'start_date', 'is_active', 'is_superuser',)}
        ),
    )

admin.site.register(CustomUser, UserAdminConfig)