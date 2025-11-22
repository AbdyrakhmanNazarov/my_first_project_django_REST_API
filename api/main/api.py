from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApartmentSerializer
from main.models import Apartment

@api_view(['GET'])
def apartments_list(request):
    apartments = Apartment.objects.all()
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def apartments_create(request):
    serializer = ApartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)