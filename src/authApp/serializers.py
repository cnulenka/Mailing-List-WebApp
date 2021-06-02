from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from authApp.models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'phone']