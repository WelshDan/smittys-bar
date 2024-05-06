from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ['id']
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
            'fields': ('email', 'password', 'start_date', 'is_active', 'is_superuser',)}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)