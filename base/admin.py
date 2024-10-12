
from django.contrib import admin
from .models import Location
from .models import Incident

# Register the Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # Customize how the model is displayed in the admin panel
    list_display = ('latitude', 'longitude', 'address', 'created_at')
    search_fields = ('address', 'latitude', 'longitude')
    list_filter = ('created_at',)

    
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'blood_group', 'height', 'weight')

from django.contrib import admin
from .models import Incident

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')  # Make sure to include fields you want to display

admin.site.register(Incident, IncidentAdmin)

