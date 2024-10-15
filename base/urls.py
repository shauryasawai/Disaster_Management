from django.urls import path
from . import views
from .views import disaster_status_view
from .views import fire_view,hospital
from .views import report_incident
from .views import report_crime, success
from .views import fetch_disaster_news


urlpatterns = [
    path('', views.login_view , name='login'),
    path('home/', views.save_location, name='home'),
    path('save_location/', views.save_location, name='save_location'),
    path('check_disaster/', disaster_status_view, name='check_disaster'),
    path('register/', views.register, name='register'),
    path('fire_safety/', views.fire_view, name='fire_view'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('hospital/', views.hospital, name='hospital'),
    path('report/', report_incident, name='report_incident'),
    path('report-crime/', report_crime, name='report_crime'),
    path('success/', success, name='success'),
    path('fetch-news/', fetch_disaster_news, name='fetch_news'),

]
