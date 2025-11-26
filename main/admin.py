from django.contrib import admin
from .models import Apartment, Block, Object

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'rooms_count', 'area', 'type', 'block')
    search_fields = ('number', 'floor')
    list_filter = ('rooms_count', 'type', 'block')
    
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'object', 'floor_count')  
    search_fields = ('name', 'object__name')
    list_filter = ('object',) 

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')