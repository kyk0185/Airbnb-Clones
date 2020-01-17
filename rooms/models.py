from django.db import models
from django_countries.fields import CountryField
from mysite import models as mysite_models


class RoomType(mysite_models.TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Amenity(mysite_models.TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Facility(mysite_models.TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HouseRule(mysite_models.TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(mysite_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    photo = models.ImageField()

    def __str__(self):
        return self.caption


class Room(mysite_models.TimeStampedModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=140)
    guests = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        'RoomType', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField('Amenity', blank=True)
    facilities = models.ManyToManyField('Facility', blank=True)
    house_rules = models.ManyToManyField('HouseRule', blank=True)

    def __str__(self):
        return self.name
