from django.urls import path

from . import  views
urlpatterns=[
    path('', views.list_vehicles,name='item_list'),
    path('create/', views.add_vehicle, name='create_item'),
    path('delete/<int:id>', views.delete, name='delete_item'),
    path('update/<int:id>', views.update, name='update_item'),
]