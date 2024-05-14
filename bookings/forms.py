from django import forms
from bookings.models import Reservation
from customers.models import User
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

        widget = {
            'table_number': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.Select(attrs={'class': 'form-control', 'step': 3600}),
            'end_time': forms.Select(attrs={'class': 'form-control'}),
        }

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