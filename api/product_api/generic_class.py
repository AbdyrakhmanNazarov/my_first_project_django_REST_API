from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import Post
from .serializers import PostSerializer
from .permissions import PostPermission

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]


