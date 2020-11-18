from django.db import models
from django.conf import settings
import datetime

class RoomModel(models.Model):
    room_type =(
        ('Standard','Standard'),
        ('Deluxe','Deluxe'),
        ('Luxury','Luxury'),
        ('Sea facing','Sea facing'),
    )
    number = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20,choices=room_type)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number} of {self.type} with {self.beds} for {self.capacity} people'

class BookingModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel,on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    checkin_time = models.TimeField(default=datetime.time(12, 00))
    checkout_time = models.TimeField(default=datetime.time(12, 00))
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.checkin} to {self.checkout}'

class demo(models.Model):
    checkin_date = models.DateField()
    checkin_time = models.TimeField(default=datetime.time(12,00))
