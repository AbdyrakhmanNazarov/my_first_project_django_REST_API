from django.contrib import admin
from product.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner",)
    search_fields = ("title", "owner",)
    list_filter = ("title", "owner",)
