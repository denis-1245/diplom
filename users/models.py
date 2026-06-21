from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Номер телефона'
    )

    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.username