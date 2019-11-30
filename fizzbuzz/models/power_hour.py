import uuid
from django.db import models

from fizzbuzz.models.music_profile import MusicProfile


class PowerHour(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)  # noqa A003
	host = models.ForeignKey(MusicProfile, on_delete=models.CASCADE, related_name='power_hours')
