from django.urls import path
from bookings import views

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
    path('get_bookings/', views.get_bookings, name='get_bookings'),
    path('edit_reservation/<int:booking_id>/', views.edit_reservation, name='edit_reservation')
    path('delete_reservation/<int:booking_id>/', views.delete_reservation, name='delete_reservation')
]