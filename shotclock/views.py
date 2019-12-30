import logging
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from shotclock import models, serializers

logger = logging.Logger(__name__)


class DefaultViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]


class UserViewSet(DefaultViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class MusicProfileViewSet(DefaultViewSet):
    queryset = models.MusicProfile.objects.all()
    serializer_class = serializers.MusicProfileSerializer


class PowerHourViewSet(DefaultViewSet):
    queryset = models.PowerHour.objects.all()
    serializer_class = serializers.PowerHourSerializer
