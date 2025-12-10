# # ==========================================================
# # Комбинированный

# from rest_framework.generics import GenericAPIView

# # from rest_framework.generics import (
# #     ListCreateAPIView,      # GET список + POST создать
# #     RetrieveUpdateDestroyAPIView,  # GET один + PUT/PATCH + DELETE
# # )
# # ==========================================================

# from rest_framework.generics import (
#     ListAPIView,  # GET список
#     RetrieveAPIView,  # GET один объект
#     CreateAPIView,  # POST создать
#     UpdateAPIView,  # PUT/PATCH обновить
#     DestroyAPIView,  # DELETE удалить
# )
# from main.models import Apartment, Block, Object
# from .serializers import ApartmentSerializer, BlockSerializer, ObjectModelSerializer


# class ApartmentList(ListAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     # pagination_class = None


# class ApartmentDetail(RetrieveAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     lookup_field = "pk"  # или 'id', по умолчанию 'pk'


# # Создание апартамента (POST)
# class ApartmentCreate(CreateAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer


# # Обновление апартамента (PUT/PATCH)
# class ApartmentUpdate(UpdateAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     lookup_field = "pk"


# # Удаление апартамента (DELETE)
# class ApartmentDelete(DestroyAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     lookup_field = "pk"


# # ==========================================================
# # Комбинированный
# # ==========================================================

# # # GET список + POST создать
# # class ApartmentListCreate(ListCreateAPIView):
# #     queryset = Apartment.objects.all()
# #     serializer_class = ApartmentSerializer

# # # GET один + PUT/PATCH + DELETE
# # class ApartmentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
# #     queryset = Apartment.objects.all()
# #     serializer_class = ApartmentSerializer
# #     lookup_field = 'pk'

# # ==========================================================
# # block
# # ==========================================================
# class BlockList(ListAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     # pagination_class = None

# class BlockDetail(RetrieveAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     lookup_field = "pk"  # или 'id', по умолчанию 'pk'

# class BlockCreate(CreateAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer

# class BlockUpdate(UpdateAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     lookup_field = "pk"

# class BlockDelete(DestroyAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     lookup_field = "pk"

# # ==========================================================
# # object
# # ==========================================================

# class ObjectList(ListAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectModelSerializer
#     # pagination_class = None

# class ObjectDetail(RetrieveAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectModelSerializer
#     lookup_field = "pk"  # или 'id', по умолчанию 'pk'

# class ObjectCreate(CreateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectModelSerializer

# class ObjectUpdate(UpdateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectModelSerializer
#     lookup_field = "pk"

# class ObjectDelete(DestroyAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectModelSerializer
#     lookup_field = "pk"

# # ==========================================================