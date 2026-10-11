from django.shortcuts import render
from habits.models import Habit
from django.utils import timezone
from checkins.models import CheckIn


def home(request):

    if request.user.is_authenticated:
        habits = request.user.habits.all()

    else:
        habits = Habit.objects.none()

    today = timezone.localdate()

    for habit in habits:
        habit.today_checkin = habit.checkins.filter(
            date=today
        ).first()

        habit.checkin_history = habit.checkins.order_by('-date')

    return render(request, 'home.html', {'habits': habits})
