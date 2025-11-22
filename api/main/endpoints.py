from django.urls import path
from .api import apartments_list, apartments_create

urlpatterns = [
    path('apartments-list/', apartments_list, name='apartments-list'),
    path('apartments-create', apartments_create, name='apartments-create'),
]