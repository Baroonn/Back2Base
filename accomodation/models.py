from django.db import models
from django.contrib.auth import get_user_model
import datetime

from django.db.models.deletion import SET_NULL

User = get_user_model()
ACCOMODATION_CATEGORY = [
   
]

# Create your models here.
class Accomodation(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    lga = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    agent = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class AccomodationImages(models.Model):
    image_id = models.CharField(max_length=100, primary_key=True)
    accomodation = models.ForeignKey(Accomodation, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.image_id