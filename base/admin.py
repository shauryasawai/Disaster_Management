
from django.contrib import admin
from .models import Location

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

# police/admin.py
from django.contrib import admin
# police/admin.py
from django.contrib import admin
from .models import IncidentReport

class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('description', 'timestamp', 'media')
    search_fields = ('description',)
    list_filter = ('timestamp',)

admin.site.register(IncidentReport, IncidentReportAdmin)


# admin.py
from django.contrib import admin
from .models import CrimeReport

class CrimeReportAdmin(admin.ModelAdmin):
    list_display = ('crime_type', 'location', 'reported_at', 'is_anonymous')
    list_filter = ('crime_type', 'reported_at', 'is_anonymous')
    search_fields = ('crime_type', 'location', 'description')
    ordering = ('-reported_at',)

admin.site.register(CrimeReport, CrimeReportAdmin)

# admin.py
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Columns to display
    search_fields = ('name', 'email')  # Add search functionality for name and email

admin.site.register(Contact, ContactAdmin)
