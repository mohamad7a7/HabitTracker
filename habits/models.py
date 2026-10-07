from django.conf import settings
from django.db import models


class Habit(models.Model):
    FRQ_D = 'D'
    FRQ_O = 'O'
    FRQ_M = 'M'
    FRQ_CHOICES = [
        (FRQ_O, 'یکبار'),
        (FRQ_M, 'ماهانه'),
        (FRQ_D, 'روزانه'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits'
    )

    title = models.CharField(max_length=100)

    frequency = models.CharField(
        max_length=1,
        choices=FRQ_CHOICES,
        default='D'
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    time = models.TimeField()

    once_date = models.DateField(
        null=True,
        blank=True
    )

    day_of_month = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
