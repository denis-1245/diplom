from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    save_on_top = True

    fieldsets = (
        ('Данные пользователя', {'fields': ('username', 'password', 'email', 'phone_number')}),
        ('Доступ', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Служебная информация', {'fields': ('last_login', 'date_joined'), 'classes': ('collapse',)}),
    )
