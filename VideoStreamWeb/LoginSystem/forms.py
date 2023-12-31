from LoginSystem.models import *
from django import forms

class ProfileUploadForm(forms.ModelForm):
    class Meta():
        model = User_Profile
        fields = ['profile_pic',]

