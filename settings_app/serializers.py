from rest_framework import serializers
from habits.models import Habit, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name']


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['user', 'place', 'time', 'action', 'is_rewarding_habit', 'related_habit', 'frequency', 'reward',
                  'time_required', 'is_public', 'status']


class PublicHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['place', 'time', 'action', 'frequency', 'time_required']
