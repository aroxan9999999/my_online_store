from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullName = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='get_avatar_url', null=True, blank=True)

    def __str__(self):
        return self.username

    def get_avatar_url(instance, filename):
        return f"avatars/{instance.username}/{filename}"
