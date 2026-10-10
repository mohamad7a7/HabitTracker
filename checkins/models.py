from django.db import models
from habits.models import Habit


class CheckIn(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name='checkins'
    )

    date = models.DateField()

    is_done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['habit', 'date'],
                name='unique_checkin_per_habit_date'
            )
        ]
