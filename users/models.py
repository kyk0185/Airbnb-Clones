from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    username = models.EmailField(
        max_length=50, null=False, unique=True, default='')
    password = models.CharField(
        unique=True, null=False, max_length=100, default='')
    superhost = models.BooleanField(default=False)
    bio = models.TextField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username
