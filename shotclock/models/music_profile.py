from django.contrib.auth.models import User
from django.db import models
from shotclock.models import BaseModel


class MusicProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='music_profile')
