from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
from accounts.managers import UserManager


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-date_joined',)

    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('support', 'Служба поддержки'),
    )

    username = None  # отключаем username
    email = models.EmailField('электронная почта', unique=True)
    phone_number = PhoneNumberField('Номер телефона', null=True, blank=True)
    full_name = models.CharField('ФИО', max_length=200)
    role = models.CharField(
        'Роль пользователя',
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class OTPVerification(models.Model):
    email = models.EmailField('Электронная почта', blank=True, null=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def is_expired(self):
        return (now() - self.created_at).seconds > 300

    def __str__(self):
        return f"{self.email} - {self.code}"
