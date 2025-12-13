from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .class_api import ApartmentViewSet, ObjectViewSet, BlockViewSet

router=DefaultRouter()
router.register('apartments', ApartmentViewSet, basename='apartments')
router.register('objects', ObjectViewSet, basename='objects')
router.register('blocks', BlockViewSet, basename='blocks')

urlpatterns = [
    path('', include(router.urls))
]







# from django.urls import path
# # from .api import (
# #     apartments_list,
# #     apartments_create,
# #     apartments_detail,
# #     blocks_detail,
# #     blocks_list,
# #     blocks_create,
# #     objects_list,
# #     objects_detail,
# #     objects_create,
# # )
# from .generic_main_api import (
#     #=============
#     # apartament
#     ApartmentList,
#     ApartmentDetail,
#     ApartmentCreate,
#     ApartmentUpdate,
#     ApartmentDelete,
#     #=============
#     # block
#     BlockList,
#     BlockDetail,
#     BlockCreate,
#     BlockUpdate,
#     BlockDelete,
#     #=============
#     # object
#     ObjectList,
#     ObjectDetail,
#     ObjectCreate,
#     ObjectUpdate,
#     ObjectDelete,
# )

# urlpatterns = [
#     # path('apartments-list/', apartments_list, name='apartments-list'),
#     # path('apartments-create/', apartments_create, name='apartments-create'),
#     # path('apartments-detail/<int:pk>/', apartments_detail, name='apartments-detail'),
#     # path('blocks-detail/<int:pk>/', blocks_detail, name='blocks-detail'),
#     # path('blocks-create/', blocks_create, name='blocks-create'),
#     # path('blocks-list/', blocks_list, name='blocks-list'),
#     # path('objects-detail/<int:pk>/', objects_detail, name='objects-detail'),
#     # path('objects-create/', objects_create, name='objects-create'),
#     # path('objects-list/', objects_list, name='objects-list'),
#     #==================================================
#     # apartment
#     path("apartments_list", ApartmentList.as_view(), name="apartmnets_list"),
#     path("apartment_detail", ApartmentDetail.as_view(), name="apartmnet_detail"),
#     path("apartment_create", ApartmentCreate.as_view(), name="apartmnet_create"),
#     path("apartment_update", ApartmentUpdate.as_view(), name="apartmnet_update"),
#     path("apartment_delete", ApartmentDelete.as_view(), name="apartmnet_delete"),
#     #==================================================
#     # block
#     path("blocks_list", BlockList.as_view(), name="blocks_list"),
#     path("block_detail", BlockDetail.as_view(), name="block_detail"),
#     path("block_create", BlockCreate.as_view(), name="block_create"),
#     path("block_update", BlockUpdate.as_view(), name="block_update"),
#     path("block_delete", BlockDelete.as_view(), name="block_delete"),
#     #==================================================
#     # object
#     path("objects_list", ObjectList.as_view(), name="objects_list"),
#     path("object_detail", ObjectDetail.as_view(), name="object_detail"),
#     path("object_create", ObjectCreate.as_view(), name="object_create"),
#     path("object_update", ObjectUpdate.as_view(), name="object_update"),
#     path("object_delete", ObjectDelete.as_view(), name="object_delete"),
# ]



