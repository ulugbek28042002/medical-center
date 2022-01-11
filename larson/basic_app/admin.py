from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from . import models

admin.site.register(models.Contact)
admin.site.register(models.Footer)
admin.site.register(models.About)


class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'phone', 'is_staff')
    ordering = ('name', 'phone')

    fieldsets = (
        (None,
         {'fields': ('name', 'phone', 'image', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}),
        # ('Group Permissions', {'classes': ('collapse',), 'fields': ('group', 'user_permissions',)})

    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': (
            'name', 'phone', 'image', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',)}),
    )


admin.site.register(models.User, CustomUserAdmin)
