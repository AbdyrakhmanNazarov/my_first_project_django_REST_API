from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from accounts.models import User, PasswordResetCode
from django.conf import settings
import random
from datetime import timedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")
        
        token, _= Token.objects.get_or_create(user=user)
        return {"token" : token.key, "email" : user.email}
        
class LogoutSerializer(serializers.Serializer):
    pass

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password) 
        Token.objects.create(user=user)
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "phone_number")
        read_only_fields = ("email",)


class FunctionChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only = True)
    new_password = serializers.CharField(write_only = True, validators = [validate_password])

    def validate(self, attrs):
        user = self.context["request"].user 
        if not user.check_password(attrs.get("old_password")):
            raise serializers.ValidationError("Старый пароль неверен")
        return attrs

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user    

class GenericChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only = True)
    new_password = serializers.CharField(write_only = True, validators = [validate_password])

    def validate(self, attrs):
        user = self.context["request"].user 
        if not user.check_password(attrs.get("old_password")):
            raise serializers.ValidationError("Старый пароль неверен")
        return attrs
    

class DeactivateSerializer(serializers.Serializer):
    confirm = serializers.BooleanField(required=True)
    
    def validate_confirm(self, value):
        if not value:
            raise serializers.ValidationError(
                "Необходимо подтвердить деактивацию"
            )
        return value

class ActivateSerializer(serializers.Serializer):
    pass


class SendMailSerializer(serializers.Serializer):
    to_email = serializers.EmailField()
    text = serializers.CharField()

    def create(self, validated_data):
        from django.core.mail import send_mail

        send_mail(
            subject="Test Email",
            message=validated_data['text'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[validated_data['to_email']],
            fail_silently=False
        )
        return validated_data
    

User = get_user_model()

class SendResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        email = validated_data["email"]

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Пользователь не найден")

        code = str(random.randint(1000, 9999))

        PasswordResetCode.objects.create(
            user=user,
            code=code
        )

        send_mail(
            subject="Сброс пароля",
            message=f"Ваш код для сброса пароля: {code}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )

        return {"email": email}


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=4)
    new_password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        email = validated_data["email"]
        code = validated_data["code"]
        new_password = validated_data["new_password"]

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Пользователь не найден")

        reset_code = PasswordResetCode.objects.filter(
            user=user,
            code=code
        ).order_by("-created_at").first()

        if not reset_code:
            raise serializers.ValidationError("Неверный код")

        if reset_code.created_at < timezone.now() - timedelta(minutes=10):
            raise serializers.ValidationError("Код истёк")

        user.set_password(new_password)
        user.save()

        PasswordResetCode.objects.filter(user=user).delete()

        return {"detail": "Пароль успешно изменён"}
