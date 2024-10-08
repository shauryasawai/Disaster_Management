from django.db import models

class Location(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)  # To store the formatted address
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location ({self.latitude}, {self.longitude})"

class SatelliteImage(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='satellite_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Satellite Image for Location: {self.location.address}'
    


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
    # Link to Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal information
    age = models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ], blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Height in cm
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Weight in kg

    # Health information
    allergies = models.TextField(blank=True, null=True)  # Any allergies the user may have
    injuries = models.TextField(blank=True, null=True)  # Past injuries or operations

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Optionally, signal to create or update UserProfile when User is created
