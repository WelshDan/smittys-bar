from django.shortcuts import render
from django.http import HttpResponse


def reserve_table(request):
        submitted = False
        active_booking = Falseform = TableBookingForm()