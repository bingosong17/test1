from .models import Firm
from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        # fields = ['url', 'username', 'email', 'groups']
        exclude = ['is_active', 'create_time']