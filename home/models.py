from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Amenities(BaseModel):
    aminity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.aminity_name
    
class Hotels(BaseModel):
    hotel_name = models.CharField(max_length=200)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)

    def __str__(self):
        return self.hotel_name
    
class HotelImages(BaseModel):
    hotel = models.ForeignKey(Hotels, related_name='hotel_images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hotel")

class HotelBookings(BaseModel):
    hotel = models.ForeignKey(Hotels, related_name="hotel_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=100, choices=(('Pre Paid','Pre Paid'),('Post Paid', 'Post Paid')))

# Models end here