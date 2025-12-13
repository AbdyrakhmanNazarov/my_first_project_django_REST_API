from django_filters import FilterSet, NumberFilter, ChoiceFilter, CharFilter, ModelChoiceFilter
from main.models import Apartment, Block, Object


class ApartmentFilter(FilterSet):
    floor = NumberFilter(field_name='floor', lookup_expr='exact')
    floor_min = NumberFilter(field_name='floor', lookup_expr='gte')
    floor_max = NumberFilter(field_name='floor', lookup_expr='lte')

    rooms_count = NumberFilter(field_name='rooms_count', lookup_expr='exact')

    area_min = NumberFilter(field_name='area', lookup_expr='gte')
    area_max = NumberFilter(field_name='area', lookup_expr='lte')

    type = ChoiceFilter(field_name='type', choices=Apartment.APARTMENT_TYPES)

    block = ModelChoiceFilter(field_name='block', queryset=Block.objects.all())
    block_type = ChoiceFilter(field_name='block__type', choices=Block.BLOCK_TYPES)

    object = ModelChoiceFilter(field_name='block__object', queryset=Object.objects.all())

    class Meta:
        model = Apartment
        fields = []


class ObjectFilter(FilterSet):
    class Meta:
        model = Object
        fields = []


class BlockFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    floor_count_min = NumberFilter(field_name='floor_count', lookup_expr='gte')
    floor_count_max = NumberFilter(field_name='floor_count', lookup_expr='lte')

    type = ChoiceFilter(field_name='type', choices=Block.BLOCK_TYPES)
    object = ModelChoiceFilter(field_name='object', queryset=Object.objects.all())

    class Meta:
        model = Block
        fields = []
