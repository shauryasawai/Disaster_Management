
from django.contrib import admin
from .models import Location, SatelliteImage

# Register the Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # Customize how the model is displayed in the admin panel
    list_display = ('latitude', 'longitude', 'address', 'created_at')
    search_fields = ('address', 'latitude', 'longitude')
    list_filter = ('created_at',)
    
@admin.register(SatelliteImage)
class SatelliteImageAdmin(admin.ModelAdmin):
    list_display = ('location', 'description')
