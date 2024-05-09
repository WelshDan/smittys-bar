from django import forms
from bookings.models import Reservation
from users.models import User
from .widgets import  DatePickerInput, TimePickerInput
from django.core.exceptions import ValidationError


class TableBookingForm(forms.ModelForm):
    # widgets link to widgets file
    date = forms.DateField(widget=DatePickerInput)
    start_time = forms.TimeField(widget=TimePickerInput)
    end_time = forms.TimeField(widget=TimePickerInput)

    class Meta:
        model = Reservation
        fields = ('table_number', 'date', 'start_time', 'end_time')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            try:
                current_user = User.objects.get(username=user.username)
                self.fields['username'].initial = current_user
            except User.DoesNotExist:
                pass

    def clean(self):
        cleaned_data = super().clean()
        table_number = cleaned_data.get('table_number')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        instance = self.instance

        check_bookings = Reservation.objects.filter(
            table_number=table_number,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time,
            active_booking=True
        )
        
        if instance and instance.pk:
            check_bookings = check_bookings.exclude(pk=instance.pk)

        if check_bookings.exists():
            raise ValidationError("Double booked! The table is booked for that time on that date")

        return cleaned_data