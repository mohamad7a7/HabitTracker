from rest_framework import serializers
from habits.models import Habit
from checkins.models import CheckIn

'''define habit serializers rules and fields'''


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit

        fields = [
            'id',
            'title',
            'frequency',
            'start_date',
            'time',
            'once_date',
            'day_of_month',
            'is_active',
            'created_at',
        ]

        read_only_fields = ['id', 'created_at']

        extra_kwargs = {
            'time': {
                'error_messages': {
                    'required': 'وارد کردن ساعت انجام الزامی است.',
                }
            }
        }

    def validate(self, attrs):
        instance = self.instance

        current_frequency = (
            instance.frequency
            if instance is not None
            else Habit.FRQ_D
        )

        frequency = attrs.get('frequency', current_frequency)

        current_start_date = (
            instance.start_date
            if instance is not None
            else None
        )

        start_date = attrs.get('start_date', current_start_date)

        current_once_date = (
            instance.once_date
            if instance is not None
            else None
        )

        once_date = attrs.get('once_date', current_once_date)

        current_day_of_month = (
            instance.day_of_month
            if instance is not None
            else None
        )

        day_of_month = attrs.get(
            'day_of_month',
            current_day_of_month
        )

        if frequency == Habit.FRQ_O:
            if not once_date:
                raise serializers.ValidationError({
                    'once_date': ' انتخاب تاریخ یکباره الزامی است'
                })

            attrs['start_date'] = None
            attrs['day_of_month'] = None

        elif frequency == Habit.FRQ_D:
            if not start_date:
                raise serializers.ValidationError({
                    'start_date': 'انتخاب تاریخ شروع الزامی است.'
                })

            attrs['once_date'] = None
            attrs['day_of_month'] = None

        elif frequency == Habit.FRQ_M:
            if day_of_month is None:
                raise serializers.ValidationError({
                    'day_of_month': 'وارد کردن روز ماه الزامی است.'
                })

            if not 1 <= day_of_month <= 31:
                raise serializers.ValidationError({
                    'day_of_month': 'روز ماه باید بین 1 تا 31 باشد.'
                })

            attrs['once_date'] = None
            attrs['start_date'] = None

        else:
            raise serializers.ValidationError({
                'frequency': 'نوع تکرار انتخاب‌شده معتبر نیست.'
            })

        return attrs


'''define checkins serializers rules and fields'''


class CheckInSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn

        fields = [
            'id',
            'habit',
            'date',
            'is_done',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
        ]
