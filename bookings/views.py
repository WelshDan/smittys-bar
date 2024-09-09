from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import TableBookingForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from datetime import datetime


@login_required
def remove_old_bookings(user):
    active_bookings = Reservation.objects.filter(username=user, active_booking=True)
    for booking in active_bookings:
        booking_end = datetime.combine(booking.date, booking.end_time)

        if booking_end < timezone.now():
            booking.active_booking=False
            booking.save()


@login_required
def reserve_table(request):
    submitted = False
    active_booking = False
    remove_old_bookings(request.user)
    form = TableBookingForm()
    user_bookings = Reservation.objects.filter(username=request.user, active_booking=True)
    if request.method == "POST":
        form = TableBookingForm(request.POST)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Your booking was successful")
            return HttpResponseRedirect('/bookings/reserve_table/')
    else:
        form = TableBookingForm()
        if 'submitted' in request.GET:
            submitted = True
            active_booking = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted, 'bookings':user_bookings})


@login_required
def edit_reservation(request, booking_id):
    remove_old_bookings(request.user)
    user_bookings = Reservation.objects.filter(username=request.user, active_booking=True)
    booking = Reservation.objects.get(pk=booking_id)
    form = TableBookingForm(instance=booking)
    if request.method == "POST":
        form = TableBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.info(request, "You have amended your booking")
            return redirect('reserve_table')
    return render(request, 'edit_reservation.html', {'form':form, 'booking': booking, 'bookings':user_bookings})


@login_required
def delete_reservation(request, booking_id):
        booking = Reservation.objects.get(pk=booking_id)
        booking.delete()
        messages.success(request, "Your booking was deleted")
        return redirect('reserve_table')


@login_required
def get_bookings(request):
    remove_old_bookings(request.user)
    if request.user.is_superuser:
            bookings = Reservation.objects.all()
    else:
            bookings = Reservation.objects.filter(username=request.user, active_booking=True)
    return render(request, 'booktable.html', {'bookings': bookings})


def get_booktable(request):
    return render(request, 'booktable.html')


def get_base(request):
        return render(request, 'base.html')


def get_index(request):
        return render(request, 'index.html')


def get_signup(request):
        return render(request, 'account_signup.html')


def get_login(request):
        return render(request, 'account_login.html')