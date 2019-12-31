import logging

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from social_django.utils import load_backend, load_strategy
from shotclock import models, serializers

logger = logging.Logger(__name__)

SOCIAL_AUTH_PROVIDER = 'spotify'


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


class SocialAuth(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        redirect = request.path

        try:
            access_token = request.data['access_token']
        except KeyError:
            return Response({'detail': "'access_token' is required."}, status=status.HTTP_400_BAD_REQUEST)

        strategy = load_strategy(request)
        backend = load_backend(strategy, SOCIAL_AUTH_PROVIDER, redirect)
        request.social_auth_backend = backend

        try:
            user = backend.do_auth(access_token, expires=None, *args, **kwargs)
            user_serializer = serializers.UserSerializer(user, context={'request': request})
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
