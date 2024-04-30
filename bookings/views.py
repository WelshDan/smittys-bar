from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Reservation
from .forms import TableBookingForm


def reserve_table(request):
        submitted = False
        active_booking = False
        form = TableBookingForm()
        user_bookings = Reservation.objects.filter(email=request.user.email).filter(active_booking=True)

        if request.method == "POST":
                form = TableBookingForm(request.POST, user=request.user)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/booktable')
        else:
                form = TableBookingForm(user=request.user)
                if 'submitted' in request.GET:
                        submitted = True
                        active_booking = True
        return render(request, 'booktable.html', {'form':form, 'submitted':submitted, 'bookings':user_bookings})