# forms.py
from django import forms

class CoordinateForm(forms.Form):
    start_x = forms.IntegerField(label='Start X')
    start_y = forms.IntegerField(label='Start Y')
    goal_x = forms.IntegerField(label='Goal X')
    goal_y = forms.IntegerField(label='Goal Y')
    
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(forms.ModelForm):
    # Form for updating the built-in User model (e.g., first name, last name, email)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
        
        
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'age', 'contact_no', 'emergency_contact_no', 
            'blood_group', 'height', 'weight', 
            'allergies_reactions', 'past_injuries_operations'
        ]

from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['description', 'media']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the incident...',
                'required': True,
                'id': 'incident-description',
                'rows': 5,
                'cols': 40
            }),
            'media': forms.ClearableFileInput(attrs={'accept': 'image/*,video/*'})
        }
