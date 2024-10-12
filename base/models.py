from django.db import models

class Location(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)  # To store the formatted address
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location ({self.latitude}, {self.longitude})"



class NaturalDisaster(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    disaster_type = models.CharField(max_length=100)
    description = models.TextField()
    event_time = models.DateTimeField()

    def __str__(self):
        return f'{self.disaster_type} near {self.latitude}, {self.longitude}'

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    contact_no = models.CharField(max_length=15, null=True)
    emergency_contact_no = models.CharField(max_length=15, null=True)
    blood_group = models.CharField(max_length=5)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    allergies_reactions = models.TextField(blank=True, null=True)  # Correct field name
    past_injuries_operations = models.TextField(blank=True, null=True)  # Correct field name

    def __str__(self):
        return f"{self.user.username}'s Profile"