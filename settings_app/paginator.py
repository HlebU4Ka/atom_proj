from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from habits.models import Habit
from django.shortcuts import render


def habit_list(request):
    habits_list = Habit.objects.all()
    paginator = Paginator(habits_list, 5)  # По 5 привычек на страницу

    page = request.GET.get('page')
    try:
        habits = paginator.page(page)
    except PageNotAnInteger:
        habits = paginator.page(1)
    except EmptyPage:
        habits = paginator.page(paginator.num_pages)

    return render(request, 'habit_list.html', {'habits': habits})
