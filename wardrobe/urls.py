from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('log/', views.log, name='log'),
    path('item/', views.item, name='item'),
    path('edit/', views.edit, name='edit'),
]