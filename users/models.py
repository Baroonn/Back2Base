from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class CustomUserManager(BaseUserManager):

#     def create_user(self, email, state, username, password=None, **kwargs):
#         if not email:
#             raise ValueError('Email field is required')

#         email = self.normalize_email(email)
#         user = self.model(email=email, state=state, username=username, **kwargs)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, state, username, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         return self.create_user(email, state, username, password, **extra_fields)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)
    state = models.CharField(max_length=30)
    image = models.CharField(max_length=40)
    no_of_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.username

