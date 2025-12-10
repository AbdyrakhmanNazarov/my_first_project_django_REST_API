from django.contrib import admin
from .models import (Apartment, 
Block, 
Object, 
ObjectImage, 
BlockImage, 
ApartmnentImage,
)

# ======================================================
# Inline (Block)
# ======================================================
class BlockInline(admin.StackedInline):
    model = Block
    extra = 1

# ======================================================
# Images (Block, Object, Apartment)
# ======================================================
class ObjectImageInline(admin.TabularInline):
    model = ObjectImage
    extra = 1

class BlockImageInline(admin.TabularInline):
    model = BlockImage
    extra = 1    

class ApartmentImageInline(admin.TabularInline):
    model = ApartmnentImage
    extra = 1

# ======================================================
# ADMIN_PANEL (Block, Object, Apartment)
# ======================================================

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("number", "floor", "rooms_count", "area", "type", "block")
    search_fields = ("number", "floor")
    list_filter = ("rooms_count", "type", "block")
    inlines = [ApartmentImageInline,]

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "object", "floor_count")
    search_fields = ("name", "object__name")
    list_filter = ("object",)
    inlines = [BlockImageInline,]

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")
    inlines = [ObjectImageInline, BlockInline]
