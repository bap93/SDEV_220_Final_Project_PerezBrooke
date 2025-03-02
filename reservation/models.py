from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    first_name = models. CharField(max_length= 50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length= 250)
    phone_number = PhoneNumberField()
    age = models.PositiveIntegerField()
    
class ReservationRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    party_size = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(default=1)

class Boat(models.Model):
    boat_type = models.CharField(max_length= 250)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.boat_type

class ReservationBoat(models.Model):
    reservation = models.ForeignKey(ReservationRequest, on_delete=models.CASCADE)
    boat_type = models.ForeignKey(Boat, on_delete=models.CASCADE)