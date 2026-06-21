from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Service

def service_list(request):
    # Начинаем с доступных услуг
    services = Service.objects.filter(is_available=True)

    # Получение уникальных категорий для фильтрации в шаблоне
    all_categories = services.values_list('category', flat=True).distinct()

    # Обработка поиска по имени или описанию
    query = request.GET.get('q')
    if query:
        services = services.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()

    # Обработка фильтрации по категории
    category_filter = request.GET.get('category')
    if category_filter and category_filter != 'all':
        services = services.filter(category=category_filter)

    # Сортируем результат
    services = services.order_by('category', 'name')

    context = {
        'services': services,
        'title': 'Каталог услуг',
        'current_category': category_filter,
        'all_categories': all_categories,
        'query': query,
    }
    return render(request, 'services/service_list.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_available=True)

    context = {
        'service': service,
        'title': service.name
    }
    return render(request, 'services/service_detail.html', context)