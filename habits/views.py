from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import HabitForm
from .models import Habit


@login_required
def create_habit(request):

    if request.method == 'POST':
        form = HabitForm(request.POST)

        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()

            return redirect('home')

    else:
        form = HabitForm()

    return render(
        request, 'create_habit.html', {'form': form}
    )


@login_required
def delete_habit(request, habit_id):

    habit = get_object_or_404(
        Habit,
        id=habit_id,
        user=request.user
    )

    if request.method == 'POST':
        habit.delete()
        return redirect('home')
