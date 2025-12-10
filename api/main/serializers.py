from rest_framework import serializers
from main.models import Apartment, Block, Object

# class BlockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Block
#         fields = "__all__"

    # name = serializers.CharField()
    # floor_count = serializers.IntegerField()
    # object = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())
    # type = serializers.ChoiceField(choices=Block.BLOCK_TYPES, default='elit') 

    # def create(self, validated_data): 
    #     return Block.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)  
    #     instance.floor_count = validated_data.get('floor_count', instance.floor_count)  
    #     instance.object = validated_data.get('object', instance.object) 
    #     instance.type = validated_data.get('type', instance.type)  
    #     instance.save()
    #     return instance

class BlockModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"

class ObjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class ApartmentListSerializer(serializers.ModelSerializer):
    block = BlockModelSerializer(many=False)
    class Meta:
        model = Apartment
        # fields = '__all__'
        # fields = ('id', 'number', 'floor', 'area', 'image', 'rooms_count')
        fields = ('id', 'number', 'floor', 'area', 'image', 'rooms_count', 'block')

class ApartmentDetailSerializer(serializers.ModelSerializer): 
    block_name = serializers.CharField(source='block.name', read_only=True)
    block_id = serializers.IntegerField(source='block.id', read_only=True)
    object_name = serializers.CharField(source= 'block.object.name', read_only=True)
    object_address = serializers.CharField(source= 'block.object.address', read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'
        # exclude = ('block',)

class ApartmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
    
    

# class ApartmentSerializer(serializers.Serializer):         
    # id = serializers.IntegerField(read_only=True)
    # number = serializers.IntegerField()
    # floor = serializers.IntegerField()
    # rooms_count = serializers.IntegerField()  
    # area = serializers.FloatField()
    # image = serializers.ImageField(required=False, allow_null=True)
    # type = serializers.ChoiceField(choices=Apartment.APARTMENT_TYPES, default='standart')  
    # block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())

    # def validate(self, attrs):
    #     if attrs.get("area") >= 250:
    #         raise serializers.ValidationError("Площадь слишком большая")
    #     return super().validate(attrs)

    # def create(self, validated_data): 
    #     return Apartment.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.number = validated_data.get('number', instance.number)  
    #     instance.floor = validated_data.get('floor', instance.floor)  
    #     instance.rooms_count = validated_data.get('rooms_count', instance.rooms_count) 
    #     instance.area = validated_data.get('area', instance.area)  
    #     instance.image = validated_data.get('image', instance.image)  
    #     instance.type = validated_data.get('type', instance.type)  
    #     instance.block = validated_data.get('block', instance.block)
    #     instance.save()
    #     return instance
    

