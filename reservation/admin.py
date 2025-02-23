from django.contrib import admin
from .models import Boat, ReservationRequest, ReservationBoat, User

admin.site.register(Boat)
admin.site.register(ReservationRequest)
admin.site.register(ReservationBoat)
admin.site.register(User)