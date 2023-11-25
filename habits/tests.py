from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Place, Habit
from django.contrib.auth import get_user_model


class HabitModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.place = Place.objects.create(name='Home')

    def test_habit_creation(self):
        habit = Habit.objects.create(
            user=self.user,
            place=self.place,
            time=timezone.now().time(),
            action='Test Habit',
            is_rewarding_habit=False,
            related_habit=None,
            frequency=7,
            reward='Test Reward',
            time_required=60,
            is_public=False,
            status='Active'
        )
        self.assertEqual(habit.__str__(), 'Test Habit')

    def test_invalid_time_required(self):
        with self.assertRaises(ValidationError):
            Habit.objects.create(
                user=self.user,
                place=self.place,
                time=timezone.now().time(),
                action='Invalid Time Habit',
                is_rewarding_habit=False,
                related_habit=None,
                frequency=7,
                reward='Test Reward',
                time_required=121,  # Should raise a ValidationError
                is_public=False,
                status='Active'
            )

    def test_invalid_frequency(self):
        with self.assertRaises(ValidationError):
            Habit.objects.create(
                user=self.user,
                place=self.place,
                time=timezone.now().time(),
                action='Invalid Frequency Habit',
                is_rewarding_habit=False,
                related_habit=None,
                frequency=6,  # Should raise a ValidationError
                reward='Test Reward',
                time_required=60,
                is_public=False,
                status='Active'
            )

    def test_invalid_related_habit(self):
        related_habit = Habit.objects.create(
            user=self.user,
            place=self.place,
            time=timezone.now().time(),
            action='Related Habit',
            is_rewarding_habit=True,
            related_habit=None,
            frequency=7,
            reward='Related Reward',
            time_required=60,
            is_public=False,
            status='Active'
        )

        with self.assertRaises(ValidationError):
            Habit.objects.create(
                user=self.user,
                place=self.place,
                time=timezone.now().time(),
                action='Invalid Related Habit',
                is_rewarding_habit=False,
                related_habit=related_habit,  # Should raise a ValidationError
                frequency=7,
                reward='Test Reward',
                time_required=60,
                is_public=False,
                status='Active'
            )
