from rest_framework import serializers
from main.models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        # fields = '__all__'
        fields = ('id', 'number', 'floor', 'area', 'image', 'rooms_count')