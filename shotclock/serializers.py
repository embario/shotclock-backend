import logging

from django.contrib.auth.models import User

from rest_framework import serializers

from shotclock import models

logger = logging.Logger(__name__)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(source='auth_token.key')

    class Meta:
        model = User
        exclude = ('user_permissions', 'groups')


class MusicProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.MusicProfile
        fields = "__all__"


class PowerHourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PowerHour
        fields = "__all__"
