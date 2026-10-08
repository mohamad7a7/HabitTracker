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

    def clean(self):

        cleaned_data = super().clean()

        frequency = cleaned_data.get('frequency')

        if frequency == Habit.FRQ_O:
            cleaned_data['start_date'] = None
            cleaned_data['day_of_month'] = None

        elif frequency == Habit.FRQ_D:
            cleaned_data['once_date'] = None
            cleaned_data['day_of_month'] = None

        elif frequency == Habit.FRQ_M:
            cleaned_data['once_date'] = None

        return cleaned_data
