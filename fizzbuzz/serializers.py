import logging

from django.contrib.auth.models import User

from rest_framework import serializers

from fizzbuzz import models

logger = logging.Logger(__name__)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class MusicProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MusicProfile
        fields = "__all__"


class PowerHourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PowerHour
        fields = "__all__"
