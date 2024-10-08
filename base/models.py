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
