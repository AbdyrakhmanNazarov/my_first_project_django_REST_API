from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from main.models import Apartment, Object, Block
from .serializers import (
    ApartmentListSerializer,
    ApartmentDetailSerializer,
    ApartmentCreateUpdateSerializer,
    #=========================
    BlockModelSerializer,
    #=========================
    ObjectModelSerializer,
)
class ApartmentViewSet(ModelViewSet):
    queryset=Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ApartmentDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ApartmentCreateUpdateSerializer 
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()

# =======================================
class BlockViewSet(ModelViewSet):
    queryset=Block.objects.all()
    serializer_class=BlockModelSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BlockModelSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return BlockModelSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()

# =======================================
class ObjectViewSet(ModelViewSet):
    queryset=Object.objects.all()
    serializer_class=ObjectModelSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ObjectModelSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ObjectModelSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()