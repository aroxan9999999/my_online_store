from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'display_avatar')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups', 'last_login')
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('fullName', 'email', 'phone', 'display_avatar', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('display_avatar',)

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" />', obj.avatar.src.url)
        return 'No image'


admin.site.register(User, CustomUserAdmin)
