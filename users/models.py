from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')
    phone = models.CharField(max_length=15, verbose_name='телефон')
    country = models.CharField(max_length=100, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
