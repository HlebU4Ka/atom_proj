from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Habit
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HabitListView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'habits/habit_list.html'
    context_object_name = 'habits'


class HabitDetailView(LoginRequiredMixin, DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'
    context_object_name = 'habit'


class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    template_name = 'habits/habit_form.html'
    fields = ['place', 'time', 'action', 'is_rewarding_habit', 'related_habit', 'frequency', 'reward', 'time_required',
              'is_public']
    success_url = reverse_lazy('habit-list')


class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    template_name = 'habits/habit_form.html'
    fields = ['place', 'time', 'action', 'is_rewarding_habit', 'related_habit', 'frequency', 'reward', 'time_required',
              'is_public']
    success_url = reverse_lazy('habit-list')


class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'habits/habit_confirm_delete.html'
    success_url = reverse_lazy('habit-list')
