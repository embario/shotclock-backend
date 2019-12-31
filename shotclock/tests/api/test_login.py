from unittest.mock import patch

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from social_core.backends.spotify import SpotifyOAuth2


class LoginAPITests(APITestCase):
    social_login_url = '/api/v1/social-login/'

    @patch.object(SpotifyOAuth2, 'do_auth')
    def test_social_login_create_user(self, mock_auth):
        mock_auth.side_effect = lambda x, expires=None: User.objects.create(username='social_user', password='pwd')
        self.assertEqual(User.objects.count(), 0)

        resp = self.client.post(self.social_login_url, data={
            'access_token': 'TOKEN'
        }, format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(resp.data['token'])
        token = resp.data['token']
        self.assertEqual(Token.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(Token.objects.filter(key=token).exists())
        self.assertTrue(User.objects.filter(username='social_user').exists())
        self.assertEqual(User.objects.get(username='social_user').auth_token.key, token)

    @patch.object(SpotifyOAuth2, 'do_auth')
    def test_social_login_existing_user(self, mock_auth):
        exp_user = User.objects.create(username='social_user', password='pwd')
        mock_auth.return_value = exp_user
        self.assertEqual(User.objects.count(), 1)

        resp = self.client.post(self.social_login_url, data={
            'access_token': 'TOKEN'
        }, format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Token.objects.count(), 1)
        self.assertIsNotNone(resp.data['token'])
        token = resp.data['token']
        self.assertTrue(Token.objects.filter(key=token).exists())
        self.assertTrue(User.objects.filter(username='social_user').exists())
        self.assertEqual(User.objects.get(username='social_user').auth_token.key, token)

    def test_social_login_no_access_token(self):
        resp = self.client.post(self.social_login_url, data={}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resp.data['detail'], "'access_token' is required.")

    @patch.object(SpotifyOAuth2, 'do_auth')
    def test_social_login_failed(self, mock_auth):
        mock_auth.side_effect = ConnectionError("Something bad happened.")

        resp = self.client.post(self.social_login_url, data={
            'access_token': 'Something valid.',
        }, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resp.data['detail'], 'Something bad happened.')
