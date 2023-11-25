from django.urls import path
from habits.views import HabitList, HabitDelete, HabitCreate, HabitUpdate

urlpatterns = [
    path('list/', HabitList.as_view(), name='habit-list'),
    path('<int:pk>/', HabitDelete.as_view(), name='habit-detail'),
    path('create/', HabitCreate.as_view(), name='habit-create'),
    path('<int:pk>/update/', HabitUpdate.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDelete.as_view(), name='habit-delete')

]
