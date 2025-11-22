from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'rooms_count', 'area')
    search_fields = ('number', 'floor')
    list_filter = ('rooms_count',)
    
