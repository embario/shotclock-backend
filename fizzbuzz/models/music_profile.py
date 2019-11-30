import uuid
from django.contrib.auth.models import User
from django.db import models


class MusicProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)  # noqa A003
	user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='music_profile')
	
