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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Customize labels
        self.fields['password2'].label = 'Confirm Password'
        # Optionally customize other attributes
        self.fields['password1'].label = 'Password'
        # Remove help texts and labels
        for field_name, field in self.fields.items():
            field.help_text = None  # Remove help text
            field.label = ''  # Optionally remove labels
            field.widget.attrs.update({'placeholder': field_name.capitalize()})  # Add placeholders if needed

        
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
from .models import IncidentReport

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['description', 'media']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the incident...', 
                'rows': 5, 'cols': 40
            }),
        }
        
# forms.py
from django import forms
from .models import CrimeReport

class CrimeReportForm(forms.ModelForm):
    class Meta:
        model = CrimeReport
        fields = ['crime_type', 'description', 'location', 'media', 'is_anonymous']

# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
        }
