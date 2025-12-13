from django.urls import path
from .generic_class import PostDetailAPIView, PostListCreateAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view())
]
