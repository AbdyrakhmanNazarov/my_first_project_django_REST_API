from django.db import models
from django_resized import ResizedImageField

class Apartment(models.Model):
    number = models.IntegerField(verbose_name="Номер квартиры")
    floor = models.IntegerField(verbose_name="Этаж")
    rooms_count = models.IntegerField(verbose_name="Количество комнат")
    area = models.FloatField(verbose_name="Площадь в квадратных метрах")
    image = ResizedImageField(size=[800, 600], upload_to='apartments/', verbose_name="Изображение квартиры",
                              blank=True, null=True, quality=90, crop=['middle', 'center'])
    def __str__(self):
        return f"Квартира {self.number} на {self.floor} этаже с {self.rooms_count} комнатами"
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
