from django.db import models
from accounts.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название поста')
    body = models.TextField(max_length=300, verbose_name='Описание поста')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец поста'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
