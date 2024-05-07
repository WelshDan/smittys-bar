from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib import auth
from .models import Customer


class customer(admin.ModelAdmin):

    model = Customer
    readonly_fields = ['id']
    search_fields = ('username', 'email', 'id',)
    list_filter = ('username', 'email', 'id', 'date_joined', 'is_active', 'is_superuser',)
    ordering = ('-id',)
    list_display = ('username', 'email', 'id', 'date_joined', 'is_active', 'is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'id', 'date_joined',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'date_joined', 'is_active', 'is_superuser',)}
        ),
    )
    
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.register(Customer)