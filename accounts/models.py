from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from accounts.managers import UserManager
from django.utils.timezone import now

class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-date_joined',)

    ROLE_CHOISES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('supper', 'Служба поддержки'),
    )

    username = None
    email = models.EmailField(verbose_name='электронная почта', unique=True, blank=False, null=False)
    phone_number = PhoneNumberField(verbose_name='Номер телефона', null=True, blank=True)
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    role = models.CharField(max_length=20, choices=ROLE_CHOISES, default='user', verbose_name='Роль пользователя')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Return the full_name, with a space in between.
        """
        return self.full_name

    def __str__(self):
        return f'{str(self.email) or self.first_name}'
    
class OTPVerification(models.Model):
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def is_expired(self):
        return (now() - self.created_at).seconds > 300
    
    def __str__(self):
        return f"{self.email} - {self.code}"
    

# ================================================================    
# class PasswordResetCode(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     code = models.CharField(max_length=4)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.email} - {self.code}"
# ================================================================ 