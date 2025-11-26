from django.db import models
from django_resized import ResizedImageField

class Object(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название объекта')
    address = models.CharField(max_length=255, verbose_name='Адрес объекта')
    image = ResizedImageField(size=[800, 600], upload_to='objects/', verbose_name='Изображение объекта', 
                              blank=True, null=True, quality=90, crop=['middle', 'center'])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Block(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блока")
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='blocks', verbose_name='Объект')
    floor_count = models.IntegerField(verbose_name='Количество этажей в блоке')
    
    def __str__(self):
        return f"Block {self.name} of {self.object.name}"
    
    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Apartment(models.Model):
    APARTMENT_TYPES = (
        ('studio', 'Студия'),
        ('standart', 'Стандартная'),
        ('comercial', 'Коммерческая'),
        ('penthouse', 'Пентхаус'),
    )
    number = models.IntegerField(verbose_name="Номер квартиры")
    floor = models.IntegerField(verbose_name="Этаж")
    rooms_count = models.IntegerField(verbose_name="Количество комнат")
    area = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Площадь в квадратных метрах")
    image = ResizedImageField(size=[800, 600], upload_to='apartments/', verbose_name="Изображение квартиры",
                              blank=True, null=True, quality=90, crop=['middle', 'center'])
    type = models.CharField(max_length=20, choices=APARTMENT_TYPES, default='standart', verbose_name='Тип квартиры')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='apartments', verbose_name='Блок')
    
    def __str__(self):
        return f"Квартира {self.number} на {self.floor} этаже с {self.rooms_count} комнатами"
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        unique_together = ['number', 'block']
        ordering = ['block', 'floor', 'number']