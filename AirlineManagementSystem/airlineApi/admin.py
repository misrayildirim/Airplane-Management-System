from django.contrib import admin
from .models import Airplane, Flight, Reservation

admin.site.register(Airplane)
admin.site.register(Flight)
admin.site.register(Reservation)

# Register your models here.
