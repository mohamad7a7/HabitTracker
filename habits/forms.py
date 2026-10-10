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

        # ساعت برای هر سه نوع Habit الزامی است
        if not cleaned_data.get('time'):
            self.add_error(
                'time',
                'وارد کردن ساعت انجام الزامی است.'
            )

        if frequency == Habit.FRQ_O:
            cleaned_data['start_date'] = None
            cleaned_data['day_of_month'] = None

            if not cleaned_data.get('once_date'):
                self.add_error(
                    'once_date',
                    'انتخاب تاریخ Habit یک‌باره الزامی است.'
                )

        elif frequency == Habit.FRQ_D:
            cleaned_data['once_date'] = None
            cleaned_data['day_of_month'] = None

            if not cleaned_data.get('start_date'):
                self.add_error(
                    'start_date',
                    'انتخاب تاریخ شروع الزامی است.'
                )

        elif frequency == Habit.FRQ_M:
            cleaned_data['once_date'] = None
            cleaned_data['start_date'] = None

            if not cleaned_data.get('day_of_month'):
                self.add_error(
                    'day_of_month',
                    'انتخاب روز ماه الزامی است.'
                )

        return cleaned_data
