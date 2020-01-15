from django.db import models
from django_countries.fields import CountryField


class Room(models.Model):
    name = models.CharField(max_length=50,blank=False)
    discription = models.TextField()
    beds = models.IntegerField(default=0,blank=True)
    bathrooms = models.IntegerField(default=0,blank=True)
    bath = models.IntegerField(default=0,blank=True)
    price = models.IntegerField(default=0,blank=True)
    country = CountryField()
    city = models.CharField(max_length=20,default='')
    is_instantBook = models.BooleanField(default=False)
    address = models.CharField(max_length=100,blank=True)
    checkIn = models.TimeField()
    checkOut = models.TimeField()
    superhost = models.ForeignKey('users.User',on_delete=models.CASCADE,default='')
    guests = models.IntegerField(default=0,blank=False)
    
    def __str__(self):
        return self.name

    
