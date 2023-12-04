from habits.models import Habit, Place
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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


# Ваш serializers.py

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if user and user.is_active:
            data['user'] = user
        else:
            raise serializers.ValidationError("Invalid login credentials")

        return data
