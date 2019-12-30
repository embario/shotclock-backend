from django.test import TestCase
from django.contrib.auth.models import User

from shotclock.models import PowerHour, PowerHourSettings


class PowerHourTests(TestCase):

    def setUp(self):
        self.test_user, _ = User.objects.get_or_create(username='test_user', password='testpassword')

    def test_create(self):
        settings = PowerHourSettings.objects.create(
            playlist="http://my-spotify.com/api/playlists/100",
            duration=60,
            created_by=self.test_user,
            modified_by=self.test_user,
        )

        power_hour = PowerHour.objects.create(
            settings=settings,
            created_by=self.test_user,
            modified_by=self.test_user,
        )

        self.assertIsNotNone(power_hour.pk)
