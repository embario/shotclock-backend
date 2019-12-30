from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class PowerHourAPITests(APITestCase):
    power_hour_url = '/api/v1/power-hours/'

    def setUp(self):
        self.test_user, _ = User.objects.get_or_create(username='test_user', password='testpassword')

    def test_get_without_token(self):
        resp = self.client.get(self.power_hour_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_with_token(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.test_user.auth_token.key}")
        resp = self.client.get(self.power_hour_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
