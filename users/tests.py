from django.test import TestCase
from .models import CustomUser


class CustomUserTest(TestCase):
    TEST_USER_EMAIL = 'testuser@example.com'
    TEST_USER_PASSWORD = 'testpassword'
    TEST_USER_NAME = 'Test User'

    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            email=self.TEST_USER_EMAIL,
            password=self.TEST_USER_PASSWORD,
            name=self.TEST_USER_NAME
        )

    def test_create_user(self):
        # Test if the user is created successfully
        self.assertEqual(self.user.email, self.TEST_USER_EMAIL)

    def test_create_superuser(self):
        # Test if the superuser is created successfully
        admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            name='Admin User'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')

    def test_user_str_method(self):
        # Test the __str__ method of the user model
        self.assertEqual(str(self.user), self.TEST_USER_EMAIL)
