# accounts/tests/test_auth.py
from django.urls import reverse
from django.test import TestCase

class UserRegistrationTest(TestCase):
    def test_register_user(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)

class UserLoginLogoutTest(TestCase):
    def test_login_user(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 200)

class PasswordResetTest(TestCase):
    def test_password_reset(self):
        response = self.client.post(reverse('accounts:password_reset'), {
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 200)
