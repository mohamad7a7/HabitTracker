from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from habits.models import Habit
from .models import CheckIn


@login_required
@require_POST
def toggle_checkin(request, habit_id):
    habit = get_object_or_404(
        Habit,
        id=habit_id,
        user=request.user
    )

    today = timezone.localdate()

    checkin, created = CheckIn.objects.get_or_create(
        habit=habit,
        date=today,
        defaults={'is_done': True}
    )

    if not created:
        checkin.is_done = not checkin.is_done
        checkin.save(update_fields=['is_done'])

    return redirect('home')
