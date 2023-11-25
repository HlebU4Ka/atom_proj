from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Habit, Place
from settings_app.serializers import HabitSerializer, PublicHabitSerializer, PlaceSerializer
from settings_app.permissions import IsOwnerOrReadOnly, IsHabitOwner


class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitCreate(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdate(generics.RetrieveUpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsHabitOwner, IsOwnerOrReadOnly]


class HabitDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsHabitOwner, IsOwnerOrReadOnly]


class PublicHabitList(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = PublicHabitSerializer
    pagination_class = PageNumberPagination


class PlaceCreate(generics.CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
