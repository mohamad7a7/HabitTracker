from django.conf import settings
from django.db import models


class Habit(models.Model):

    class Frequency(models.TextChoices):
        ONCE = 'ONCE', 'یک‌بار'
        DAILY = 'DAILY', 'روزانه'
        MONTHLY = 'MONTHLY', 'ماهانه'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits'
    )

    title = models.CharField(max_length=100)

    frequency = models.CharField(
        max_length=10,
        choices=Frequency.choices
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
