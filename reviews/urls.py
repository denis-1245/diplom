from django.urls import path
from . import views

urlpatterns = [
    # Теперь 'reviews' будет ссылаться на функцию в views.py этого приложения
    path('', views.reviews_view, name='reviews'),
]