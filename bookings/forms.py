from django import forms
from bookings.models import Reservation
from users.models import Customer
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
                self.fields['email'].initial = user.email
            except AttributeError:
                pass

    def clean(self):
        cleaned_data = super(TableBookingForm, self).clean()
        table_number = cleaned_data.get('table_number')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        try:
            active_reservation = Reservations.objects.filter(table_number=table_number, date=date, start_time=start_time, end_time=end_time, active_booking=True).exists()
            raise ValidationError("Double booked! The table is booked for that time on that date")
        except Reservation.DoesNotExist:
            pass
        except Exception as e:
            raise ValidationError("There was an error in the process. Please try again")

        return cleaned_data