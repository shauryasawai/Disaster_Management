# forms.py
from django import forms

class CoordinateForm(forms.Form):
    start_x = forms.IntegerField(label='Start X')
    start_y = forms.IntegerField(label='Start Y')
    goal_x = forms.IntegerField(label='Goal X')
    goal_y = forms.IntegerField(label='Goal Y')
