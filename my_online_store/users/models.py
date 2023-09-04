from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullName = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    avatar = models.OneToOneField('Avatar', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Avatar(models.Model):
    src = models.ImageField(upload_to='avatar/', null=True, blank=True)
    ait = models.CharField(max_length=255)
