from django.contrib.auth.models import AbstractUser
from django.db import models

from education_platform.models import NULLABLE


class User(AbstractUser):
    username = None

    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    phone = models.CharField(max_length=50, verbose_name='номер телефон', **NULLABLE)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'



