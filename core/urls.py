from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('o-nas/', views.about_view, name='about'),
    path('uslugi/', views.service_list_view, name='service_list'),
    path('kontakty/', views.contacts_view, name='contacts'),
    path('raboty/', views.works_view, name='works'),
    path('raboty/<slug:slug>/', views.work_detail_view, name='work_detail'),
]