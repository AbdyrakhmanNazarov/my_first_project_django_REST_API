from django.urls import path
from .api import apartments_list, apartments_create, apartments_detail, blocks_detail, blocks_list, blocks_create, objects_list, objects_detail, objects_create

urlpatterns = [
    path('apartments-list/', apartments_list, name='apartments-list'),
    path('apartments-create/', apartments_create, name='apartments-create'),
    path('apartments-detail/<int:pk>/', apartments_detail, name='apartments-detail'),

    path('blocks-detail/<int:pk>/', blocks_detail, name='blocks-detail'),
    path('blocks-create/', blocks_create, name='blocks-create'),
    path('blocks-list/', blocks_list, name='blocks-list'),

    path('objects-detail/<int:pk>/', objects_detail, name='objects-detail'),
    path('objects-create/', objects_create, name='objects-create'),
    path('objects-list/', objects_list, name='objects-list'),
]