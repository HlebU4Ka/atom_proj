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
        self.assertTrue(self.user.check_password(self.TEST_USER_PASSWORD))  # Проверка, что пароль хешируется

    def test_create_superuser(self):
        # Test if the superuser is created successfully
        admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            name='Admin User'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)  # Проверка, что is_staff=True
        self.assertTrue(admin_user.is_superuser)  # Проверка, что is_superuser=True

    def test_user_str_method(self):
        # Test the __str__ method of the user model
        self.assertEqual(str(self.user), self.TEST_USER_EMAIL)

    def test_user_properties(self):
        # Test additional properties of the user model
        self.assertFalse(self.user.is_staff)  # Проверка, что is_staff=False по умолчанию
        self.assertTrue(self.user.is_active)  # Проверка, что is_active=True по умолчанию
        self.assertIsNone(self.user.telegram_chat_id)  # Проверка, что telegram_chat_id по умолчанию None
        self.assertIsNone(self.user.telegram_username)  # Проверка, что telegram_username по умолчанию None

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='invalid_email', password='testpassword', name='Test User')

    def test_weak_password(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='anotheruser@example.com', password='weakpass', name='Another User')

    def test_token_generation(self):
        token = self.user.generate_auth_token()
        self.assertIsNotNone(token)
        self.assertTrue(isinstance(token, str))

    def test_token_validation(self):
        token = self.user.generate_auth_token()
        user = CustomUser.verify_auth_token(token)
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)


class AuthenticationViewTest(TestCase):
    def test_registration_view(self):
        response = self.client.post('/register/', {'email': 'newuser@example.com', 'password': 'strongpassword'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(CustomUser.objects.get(email='newuser@example.com'))

    def test_login_view(self):
        response = self.client.post('/login/', {'email': self.TEST_USER_EMAIL, 'password': self.TEST_USER_PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in response.data)
        self.assertTrue('refresh_token' in response.data)


def test_set_telegram_info(self):
    self.user.set_telegram_info(chat_id='12345', username='telegram_user')
    self.assertEqual(self.user.telegram_chat_id, '12345')
    self.assertEqual(self.user.telegram_username, 'telegram_user')
