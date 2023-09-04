from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Avatar

User = get_user_model()


class AvatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        fields = ['src', 'ait']


    def get_src(self, obj):
        return obj.src.url


class UserSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'avatar', 'fullName']
