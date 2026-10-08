from django.shortcuts import render
from habits.models import Habit


def home(request):

    if request.user.is_authenticated:
        habits = request.user.habits.all()

    else:
        habits = Habit.objects.none()

    return render(request, 'home.html', {'habits': habits})
