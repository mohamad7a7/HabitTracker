from django import forms
from .models import Habit


'''define the form of creating a habit and rules of each field'''


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['time'].error_messages['required'] = (
            'وارد کردن ساعت انجام الزامی است.'
        )

    def clean(self):
        cleaned_data = super().clean()
        frequency = cleaned_data.get('frequency')

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

            if 'day_of_month' in cleaned_data:
                day_of_month = cleaned_data.get('day_of_month')

                if day_of_month is None:
                    self.add_error(
                        'day_of_month',
                        'وارد کردن روز ماه الزامی است.'
                    )

        elif not 1 <= day_of_month <= 31:
            self.add_error(
                'day_of_month',
                'روز ماه باید بین 1 تا 31 باشد.'
            )
        return cleaned_data
