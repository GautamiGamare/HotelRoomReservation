from django.db import models
from hotel_admin.models import hotelRooms,roomImages
import datetime

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=1000)

class bookedRooms(models.Model):
    id = models.AutoField(primary_key=True)
    roomId = models.ForeignKey(hotelRooms,on_delete=models.CASCADE)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    checkin_time = models.TimeField(default=datetime.time(12,00))
    checkout_time = models.TimeField(default=datetime.time(11, 00))
    status = models.CharField(default="Confirm",max_length=40)
    rooms = models.CharField(max_length=20,default=0)

