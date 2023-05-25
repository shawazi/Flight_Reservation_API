from django.contrib import admin
from .models import Flight, Reservation, Passenger
# Register your models here.

admin.site.register((Flight, Reservation, Passenger))
