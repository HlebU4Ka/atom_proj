from rest_framework import permissions

from habits.models import Habit
from settings_app import serializers


class IsHabitOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class PublicHabitSerializer(serializers.HabitSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'place', 'time', 'action', 'frequency', 'is_public']


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять свои объекты, но не чужие.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD или OPTIONS (операции чтения)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить запись только владельцу объекта
        return obj.user == request.user