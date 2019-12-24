import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)  # noqa A003
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, on_delete=models.PROTECT, related_name="created_%(class)s")
    modified_by = models.OneToOneField(User, on_delete=models.PROTECT, related_name="modified_%(class)s")

    class Meta:
        abstract = True
