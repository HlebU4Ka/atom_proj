from django.urls import path
from .views import HabitListView, HabitDetailView, \
    HabitCreateView, HabitUpdateView, HabitDeleteView

urlpatterns = [
    path('list/', HabitListView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('create/', HabitCreateView.as_view(), name='habit-create'),
    path('<int:pk>/update/', HabitUpdateView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDeleteView.as_view(), name='habit-delete')

]
