from django import forms
from .models import Habit


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit

        fields = [
            'title',
            'frequency',
            'start_date',
            'time',
            'once_date',
            'day_of_month',
        ]
