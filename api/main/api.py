from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ApartmentSerializer, BlockSerializer, ObjectModelSerializer
from main.models import Apartment, Block, Object

@api_view(['GET'])
def apartments_list(request):
    # apartments = Apartment.objects.all()
    # serializer = ApartmentSerializer(apartments, many=True)
    # return Response(serializer.data)

    apartments = Apartment.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 5
    result_page = paginator.paginate_queryset(apartments, request)
    serializer = ApartmentSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def apartments_create(request):
    serializer = ApartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def apartments_detail(request, pk):
    try:
        apartment = Apartment.objects.get(pk=pk)
    except Apartment.DoesNotExist:
        return Response({"detail":"Not Fount"})
    
    if request.method == "GET":
        serializer = ApartmentSerializer(apartment, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ApartmentSerializer(apartment, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        apartment.delete()
        return Response(status=204)


# ========================================

@api_view(['GET'])
def blocks_list(request):
    # apartments = Block.objects.all()
    # serializer = BlockSerializer(apartments, many=True)
    # return Response(serializer.data)

    blocks = Block.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 5
    result_page = paginator.paginate_queryset(blocks, request)
    serializer = BlockSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def blocks_create(request):
    serializer = BlockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def blocks_detail(request, pk):
    try:
        blocks = Block.objects.get(pk=pk)
    except Block.DoesNotExist:
        return Response({"detail":"Not Fount"})
    
    if request.method == "GET":
        serializer = BlockSerializer(blocks, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = BlockSerializer(blocks, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        blocks.delete()
        return Response(status=204)


# ========================================

@api_view(['GET'])
def objects_list(request):
    objects = Object.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 5
    result_page = paginator.paginate_queryset(objects, request)
    serializer = ObjectModelSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def objects_create(request):
    serializer = ObjectModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def objects_detail(request, pk):
    try:
        objects = Object.objects.get(pk=pk)
    except Object.DoesNotExist:
        return Response({"detail":"Not Fount"})
    
    if request.method == "GET":
        serializer = ObjectModelSerializer(objects, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ObjectModelSerializer(objects, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        objects.delete()
        return Response(status=204)

