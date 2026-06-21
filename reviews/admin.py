from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'car_model', 'service', 'rating', 'is_published', 'created_at')
    list_filter = ('is_published', 'rating', 'service')
    search_fields = ('user__username', 'car_model', 'service', 'text')
    readonly_fields = ('created_at',)
    list_editable = ('is_published',)
    save_on_top = True
    fieldsets = (
        ('Отзыв клиента', {
            'fields': ('user', 'car_model', 'service', 'rating', 'text')
        }),
        ('Публикация', {
            'fields': ('is_published', 'created_at')
        }),
    )
