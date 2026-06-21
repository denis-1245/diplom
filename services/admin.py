from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description', 'category')
    list_editable = ('price', 'is_available')
    ordering = ('category', 'name')
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    fieldsets = (
        ('Карточка услуги или товара', {
            'fields': ('name', 'category', 'price', 'description', 'image', 'is_available')
        }),
        ('Адрес страницы', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
    )
