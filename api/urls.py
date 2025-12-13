from django.urls import path, include

urlpatterns = [
    path('', include('api.yasg')),
    path('estate/', include('api.main.endpoints')),
    path('auth/', include('api.auth.endpoints')),
    path('product_post/', include('api.product_api.endpoints')),
]
