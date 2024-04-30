from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView

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


def edit_reservation(request, booking_id):
        user_bookings = Reservation.objects.filter(email=request.user.email).filter(active_booking=True)
        booking = Resvervation.object.get(pk=booking_id)
        form = TableBookingForm(user=request.user, instance=booking)
        if request.method == "POST":
                form = TableBookingForm(request.POST, user=request.user, instance=booking)
                if form.is_valid():
                        form.save()
                        return redirect('booktable')
        return render(request, 'edit_reservation.html', {'form':form, 'booking': booking, 'bookings':user_bookings})


def delete_reservation(request, booking_id):
        booking = Reservation.objects.get(pk=booking_id)
        booking.delete()
        return redirect('booktable')


def get_base(request):
        return render(request, 'base.html')


def get_index(request):
        return render(request, 'index.html')


def get_signup(request):
        return render(request, 'account_signup.html')


def get_login(request):
        return render(request, 'account_login.html')