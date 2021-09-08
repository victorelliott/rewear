from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('log/', views.log, name='log'),
    path('item/<int:pk>', views.item, name='item'),
    path('edit/<int:pk>', views.edit, name='edit'),
]