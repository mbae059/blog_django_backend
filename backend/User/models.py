from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, default='')

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    introduction = models.TextField(default="default")
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "User"