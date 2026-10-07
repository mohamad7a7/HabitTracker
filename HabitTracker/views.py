from django.shortcuts import render
from habits.models import Habit


def home(request):

    habits = request.user.habits.all()

    return render(request, 'home.html', {'habits': habits})
