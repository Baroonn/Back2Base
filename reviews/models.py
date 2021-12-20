from django.db import models
from django.contrib.auth import get_user_model
from accomodation.models import Accomodation

User = get_user_model()

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    accomodation = models.ForeignKey(Accomodation, related_name='reviews', on_delete=models.CASCADE)