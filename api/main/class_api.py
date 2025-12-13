from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import StandartResultsSetPagination
from main.models import Apartment, Object, Block
from .filters_apartment import ApartmentFilter, BlockFilter, ObjectFilter
from .permissions import IsAdminOrReadonly
from .serializers import (
    ApartmentListSerializer,
    ApartmentDetailSerializer,
    ApartmentCreateUpdateSerializer,
    #=========================
    BlockModelSerializer,
    #=========================
    ObjectModelSerializer,
)

# ======================================================
# Apartment (ModelView) или (ReadOnlyModelView)
# ======================================================
class ApartmentViewSet(ModelViewSet):
    queryset=Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    permission_classes = (IsAdminOrReadonly,)
    pagination_class = StandartResultsSetPagination
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ("floor", "area", "rooms_count", "type", "block__name", "block__object__name")
    filterset_class = ApartmentFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ApartmentDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ApartmentCreateUpdateSerializer 
        return super().get_serializer_class()
    
    # def get_permissions(self):
    #     if self.action in ["create", "update", "partial_update", "delete"]:
    #         return [IsAdminUser()]
    #     return super().get_permissions()

# ======================================================
# Block
# ======================================================
class BlockViewSet(ModelViewSet):
    queryset=Block.objects.all()
    serializer_class=BlockModelSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandartResultsSetPagination
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ("name", "object__name", "type", )
    filterset_class = BlockFilter


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

# ======================================================
# Object
# ======================================================
class ObjectViewSet(ModelViewSet):
    queryset=Object.objects.all()
    serializer_class=ObjectModelSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandartResultsSetPagination
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ("name",)
    filterset_class = ObjectFilter

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