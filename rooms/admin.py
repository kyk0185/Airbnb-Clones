from django.contrib import admin
from . models import Room
from rooms.amenities.models import Amenity
from rooms.facilities.models import Facility

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = ('__str__','discription','country','city','checkIn','checkOut','superhost','guests','is_instantBook')
    list_filter = ('country','city','is_instantBook')


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass