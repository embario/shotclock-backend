from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from fizzbuzz.models import BaseModel

POWER_HOUR_DEFAULT = 60


class PowerHourSettings(BaseModel):
    """ PowerHourSettings encapsulate configurations for PowerHour instances."""
    playlist = models.URLField()
    duration = models.IntegerField(default=POWER_HOUR_DEFAULT, validators=[MinValueValidator(1), MaxValueValidator(1000)])


class PowerHour(BaseModel):
    """ PowerHour is the class of selectable objects the user can choose from or create in order to play a power hour."""
    name = models.CharField(null=True, blank=True, max_length=256)
    settings = models.OneToOneField(PowerHourSettings, null=True, blank=True, on_delete=models.SET_NULL)


class PowerHourSession(BaseModel):
    """ PowerHourSession is the receipt of a PowerHour instance being played. """
    scheduled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    duration = models.TimeField(null=True, blank=True)
    power_hour = models.ForeignKey(PowerHour, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User)
