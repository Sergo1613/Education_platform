from datetime import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password']

    def create(self, validated_data):
        """Переопределение метода для сохранения хешированного пароля в БД"""
        validated_data['date_joined'] = datetime.now(tz=datetime.utcnow().tzinfo)
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'is_active']
