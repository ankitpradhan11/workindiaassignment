from django.db import models
from django.contrib.auth.models import User

class Train(models.Model):
    train_name = models.CharField(max_length=100,default="Sanghmitra Express")
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.train_name} ({self.source} -> {self.destination})'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # Correctly referencing the User model
    train = models.ForeignKey(Train, on_delete=models.CASCADE) # Correctly referencing the Train model
    seat_number = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking: {self.user} - Seat {self.seat_number} on {self.train}'
