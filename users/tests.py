from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            name='Test User'
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            name='Admin User'
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_unique_email(self):
        User = get_user_model()
        User.objects.create_user(email='test@example.com', password='testpassword', name='Test User')
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email='test@example.com', password='testpassword', name='Another User')

    def test_str_representation(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@example.com', password='testpassword', name='Test User')
        self.assertEqual(str(user), 'test@example.com')


class CustomUserModelTest(TestCase):

    def test_create_user_with_optional_fields(self):
        # Test creating a user with optional fields
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            name='Test User',
            chat_id='123456',
            telegram_username='test_user'
        )

        # Check that the user is created with the correct values
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.chat_id, '123456')
        self.assertEqual(user.telegram_username, 'test_user')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        # Test creating a superuser
        admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            name='Admin User'
        )

        # Check that the superuser is created with the correct values
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.name, 'Admin User')
        self.assertTrue(admin_user.check_password('adminpassword'))
        self.assertTrue(admin_user.is_active)