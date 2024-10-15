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
    
# police/models.py
from django.db import models

class IncidentReport(models.Model):
    description = models.TextField()
    media = models.FileField(upload_to='incident_media/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:50]
    
# models.py
from django.db import models

class CrimeReport(models.Model):
    CRIME_TYPES = [
        ('theft', 'Theft'),
        ('vandalism', 'Vandalism'),
        ('violence', 'Violence'),
        ('cybercrime', 'Cybercrime'),
    ]
    
    crime_type = models.CharField(max_length=20, choices=CRIME_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    media = models.FileField(upload_to='crime_reports/', blank=True, null=True)  # Optional
    is_anonymous = models.BooleanField(default=False)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crime_type} reported at {self.location}"


