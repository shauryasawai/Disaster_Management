from django.urls import path
from . import views
from .views import disaster_status_view
from .views import pathfinding_view

urlpatterns = [
    path('', views.save_location, name='home'),
    path('save_location/', views.save_location, name='save_location'),
    path('check_disaster/', disaster_status_view, name='check_disaster'),
    path('pathfinding/<int:image_id>/', pathfinding_view, name='pathfinding_view'),

]
