from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Hotels)
""" class phonebooks(admin.ModelAdmin):
    list_display = ['name','age','mobile','dob','email','anniversary'] """
admin.site.register(Amenities)

admin.site.register(HotelBookings)
admin.site.register(HotelImages)