from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Habit, Place
from django.core.exceptions import ValidationError

class PlaceModelTest(TestCase):
    def test_place_creation(self):
        place = Place.objects.create(name='Test Place')
        self.assertEqual(Place.objects.count(), 1)
        self.assertEqual(place.name, 'Test Place')


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            name='Test User'
        )
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))

    def test_create_superuser(self):
        admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            name='Admin User'
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            name='Test User'
        )
        self.place = Place.objects.create(name='Home')

    def test_habit_creation(self):
        habit = Habit.objects.create(
            user=self.user,
            place=self.place,
            time='12:00:00',
            action='Test Habit',
            is_rewarding_habit=False,
            time_required=60,
            frequency=7,
            reward='Test Reward',
            is_public=False,
            status='Active'
        )

        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(habit.user, self.user)
        self.assertEqual(habit.place, self.place)
        # Add more assertions based on your model fields

    def test_invalid_related_habit(self):
        habit1 = None  # инициализируем переменную
        try:
            habit1 = Habit.objects.create(
                user=self.user,
                place=self.place,
                time='12:00:00',
                action='Test Habit 1',
                is_rewarding_habit=True,
                time_required=60,
                frequency=7,
                reward='Test Reward 1',
                is_public=False,
                status='Active'
            )
        except ValidationError as e:
            self.assertEqual(str(e.message_dict['__all__'][0]), 'Вознаграждающая привычка не может иметь вознаграждения или связанной с ней привычки.')
        else:
            # Проверка, что habit1 успешно создана
            self.assertIsNotNone(habit1)

            habit2 = Habit.objects.create(
                user=self.user,
                place=self.place,
                time='12:00:00',
                action='Test Habit 2',
                is_rewarding_habit=False,
                related_habit=habit1,
                time_required=60,
                frequency=7,
                reward='Test Reward 2',
                is_public=False,
                status='Active'
            )

            with self.assertRaises(ValidationError):
                habit2.full_clean()
