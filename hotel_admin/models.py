from django.db import models
import datetime

class adminDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class roomType(models.Model):
    id=models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    images = models.ImageField(upload_to="hotelImages/")
    facility = models.CharField(max_length=300)
    capacity = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
    def __str__(self):
        return self.type

class hotelRooms(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    type = models.ForeignKey(roomType,on_delete=models.CASCADE)
    def __str__(self):
        return self.id

class roomImages(models.Model):
    id = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to="hotelImages/")
    type = models.ForeignKey(roomType, on_delete=models.CASCADE)

# class roomCapacity(models.Model):
#     id = models.AutoField(primary_key=True)
#     room = models.ForeignKey(hotelRooms, on_delete=models.CASCADE)
#     checkin_date = models.DateField()
#     checkout_date = models.DateField()


