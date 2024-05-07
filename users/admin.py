from django.contrib import admin
from .models import Customer


class customer(admin.ModelAdmin):

    model = Customer
    readonly_fields = ['id']
    search_fields = ('email', 'id',)
    list_filter = ('email', 'id', 'date_joined', 'is_active', 'is_superuser',)
    ordering = ('-id',)
    list_display = ('email', 'id', 'date_joined', 'is_active', 'is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'id', 'date_joined',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'date_joined', 'is_active', 'is_superuser',)}
        ),
    )

admin.site.register(Customer, customer)