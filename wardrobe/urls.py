from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('log/', views.log, name='log'),
    path('item/<int:item_id>', views.item, name='item'),
    path('edit/<int:item_id>', views.edit, name='edit'),
]