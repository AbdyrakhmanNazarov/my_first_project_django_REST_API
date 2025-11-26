from rest_framework import serializers
from main.models import Apartment, Block

# class ApartmentModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apartment
#         fields = '__all__'
#         # fields = ('id', 'number', 'floor', 'area', 'image', 'rooms_count')

class ApartmentSerializer(serializers.Serializer):  
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField()
    floor = serializers.IntegerField()
    rooms_count = serializers.IntegerField()  
    area = serializers.FloatField()
    image = serializers.ImageField(required=False, allow_null=True)
    type = serializers.ChoiceField(choices=Apartment.APARTMENT_TYPES, default='standart')  
    block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())

    def validate(self, attrs):
        if attrs.get("area") >= 250:
            raise serializers.ValidationError("Площадь слишком большая")
        return super().validate(attrs)

    def create(self, validated_data): 
        return Apartment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)  
        instance.floor = validated_data.get('floor', instance.floor)  
        instance.rooms_count = validated_data.get('rooms_count', instance.rooms_count) 
        instance.area = validated_data.get('area', instance.area)  
        instance.image = validated_data.get('image', instance.image)  
        instance.type = validated_data.get('type', instance.type)  
        instance.block = validated_data.get('block', instance.block)
        instance.save()
        return instance