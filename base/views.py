import requests
from django.shortcuts import render
from django.conf import settings
from .models import Location, UserProfile
import os
from django.contrib import messages
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import geopy.distance
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import login,authenticate

load_dotenv()
API_KEY = os.getenv('POSITIONSTACK_API_KEY')
# Your API key from PositionStack
@login_required
def home(request):
    return render(request, 'base/home.html')
@login_required
def save_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if latitude and longitude:
            # Make the API request to PositionStack
            api_url = f'http://api.positionstack.com/v1/reverse?access_key={API_KEY}&query={latitude},{longitude}'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                location_info = data['data'][0]['label'] if data['data'] else 'Location not found'
                
                  # Save the location to the database
                location, created = Location.objects.get_or_create(
                    latitude=latitude,
                    longitude=longitude,
                    defaults={'address': location_info}
                )
                # Render the home page with location information and satellite images
                return render(request, 'base/home.html', {
                    'latitude': latitude,
                    'longitude': longitude,
                    'location_info': location_info,
                })

    # If no POST data, just render the home page without location
    return render(request, 'base/home.html')

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if remember_me:
                request.session.set_expiry(604800)
            else:  
                request.session.set_expiry(0)   
            
            login(request, user)  
            request.session['username'] = username  
            messages.success(request, 'Login successful.')
            print("User authenticated:", user)
            print("Session username after login:", request.session.get('username'))
            
            return redirect('http://localhost:5173/') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'base/login.html')

@login_required
def profile_view(request):
    user = request.user.userprofile  
    return render(request, 'base/profile.html', {'user': user})

@login_required
def create_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('http://localhost:5173/')
    else:
        form = UserProfileForm()
    return render(request, 'base/create_profile.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            UserProfile.objects.create(user=user)  
            login(request, user) 
            return redirect('create_profile')  
    else:
        user_form = UserRegistrationForm()

    return render(request, 'base/register.html', {'user_form': user_form})

@login_required
def dashboard(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Redirect to create profile page if it doesn't exist yet
        return redirect('create_profile')
    
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Reload the dashboard with updated data
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'base/dashboard.html', {'form': form, 'profile': profile})

# ReliefWeb API URL for disasters
RELIEFWEB_API_URL = 'https://api.reliefweb.int/v1/disasters'
@login_required
# Function to check if a location is under a natural calamity using ReliefWeb API
def check_disaster(latitude, longitude):
    # Set parameters for ReliefWeb API request to get recent disasters
    params = {
        'appname': 'your-app-name',
        'filter[field]': 'status',
        'filter[value]': 'current', 
        'limit': 10  # You can increase this if needed
    }

    response = requests.get(RELIEFWEB_API_URL, params=params)
    disasters = response.json().get('data', [])

    # Iterate over disasters and check if any are near the given coordinates
    for disaster in disasters:
        disaster_fields = disaster.get('fields', {})
        disaster_location = disaster_fields.get('primary_country', {}).get('location', None)

        # If a location is available, check the distance to the given coordinates
        if disaster_location:
            disaster_lat = disaster_location['lat']
            disaster_lon = disaster_location['lon']

            # Check if the disaster is within a certain radius (e.g., 100km) of the user's location
            if is_within_radius(latitude, longitude, disaster_lat, disaster_lon, 100):
                return {
                    'is_under_calamity': True,
                    'disaster_type': disaster_fields.get('name', 'Unknown Disaster'),
                    'description': disaster_fields.get('description', 'No description available')
                }

    return {'is_under_calamity': False}


# Helper function to calculate the distance between two lat/lon points (using Haversine formula)
import math
@login_required
def is_within_radius(lat1, lon1, lat2, lon2, radius_km):
    # Calculate the distance between two lat/lon points
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    distance = geopy.distance.distance(coords_1, coords_2).km
    return distance <= radius_km

# Django view to handle the incoming POST request with coordinates
@csrf_exempt
@login_required
def disaster_status_view(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        # Check if the location is under a calamity
        result = check_disaster(latitude, longitude)

        # Pass the result to calamity_result.html
        return render(request, 'base/calamity_result.html', result)

    return render(request, 'base/calamity_result.html', {'error': 'Invalid request'})


# police/views.py
from django.shortcuts import render, redirect
from .forms import IncidentReportForm
@login_required
def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_incident')  # Redirect to the same page after submission
    else:
        form = IncidentReportForm()
    
    return render(request, 'base/police.html', {'form': form})
@login_required
def fire_view(request):
    return render(request, 'base/fire_safety.html')
@login_required
def hospital(request):
    return render(request, 'base/hospitals.html')
@login_required
def police(request):
    return render(request, 'base/police.html')

# views.py
from django.shortcuts import render, redirect
from .forms import CrimeReportForm
@login_required
def report_crime(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = CrimeReportForm()
    
    return render(request, 'base/crime_report.html', {'form': form})
@login_required
def success(request):
    return render(request, 'base/success.html')

# views.py
import requests
from django.http import JsonResponse
@login_required
def fetch_disaster_news(request):
    api_key = '14bbbb4403364fe8ae900c0fafc4ad61'
    url = f'https://newsapi.org/v2/everything?q=disaster&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()

    articles = []
    if response.status_code == 200:
        for article in data['articles']:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'date': article['publishedAt'],
                'source': article['source']['name'],
                'url': article['url']
            })
    return JsonResponse({'articles': articles})
@login_required
def wildlife(request):
    return render(request, 'base/wildlife.html')
@login_required
def disaster_recovery(request):
    return render(request, 'base/disaster_recovery.html')
@login_required
def hazard(request):
    return render(request, 'base/hazard.html')


