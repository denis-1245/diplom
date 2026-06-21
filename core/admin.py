from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Work, WorkMedia

admin.site.site_header = 'BuzzBee — панель управления'
admin.site.site_title = 'BuzzBee'
admin.site.index_title = 'Управление сайтом'

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

class WorkMediaInline(admin.TabularInline):
    model = WorkMedia
    extra = 0
    fields = ('file', 'is_image')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'is_active')
    list_filter = ('is_active', 'duration')
    search_fields = ('title', 'description', 'tags')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'main_media', 'is_active')
        }),
        ('Цена и сроки', {
            'fields': ('tags', 'duration', 'price'),
            'description': 'Теги вводятся через запятую. Например: шумоизоляция, акустика, полировка.'
        }),
        ('Адрес страницы', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
    )

    inlines = [WorkMediaInline]
