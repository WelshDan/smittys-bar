from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Reservation
from .forms import TableBookingForm


@login_required
def reserve_table(request):
    submitted = False
    active_booking = False
    current_user = User.objects.get(username=request.user.username)
    user_bookings = Reservation.objects.filter(username=current_user).filter(active_booking=True)
    form = TableBookingForm()
    if request.method == "POST":
        form = TableBookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.instance.email = current_user
            form.save()
            return HttpResponseRedirect('/booktable')
    else:
        form = TableBookingForm(user=request.user)
        if 'submitted' in request.GET:
            submitted = True
            active_booking = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted, 'bookings':user_bookings})


@login_required
def edit_reservation(request, booking_id):
    current_user = User.objects.get(email=request.user.email)
    user_bookings = Reservation.objects.filter(email=current_user).filter(active_booking=True)
    booking = Reservation.objects.get(pk=booking_id)
    form = TableBookingForm(user=request.user, instance=booking)
    if request.method == "POST":
        form = TableBookingForm(request.POST, user=request.user, instance=booking)
        if form.is_valid():
                form.instance.email = user_user
                form.save()
                return redirect('booktable')
    return render(request, 'edit_reservation.html', {'form':form, 'booking': booking, 'bookings':user_bookings})


@login_required
def delete_reservation(request, booking_id):
        booking = Reservation.objects.get(pk=booking_id)
        booking.delete()
        return redirect('booktable')


@login_required
def get_bookings(request):
        current_user = User.objects.get(email=request.user.email)
        if request.user.is_superuser:
                bookings = Reservation.objects.all()
        else:
                bookings = Reservation.objects.filter(email=user_user).filter(active_booking=True)
        return render(request, 'booktable.html', {'bookings': bookings})


def get_base(request):
        return render(request, 'base.html')


def get_index(request):
        return render(request, 'index.html')


def get_signup(request):
        return render(request, 'account_signup.html')


def get_login(request):
        return render(request, 'account_login.html')