from django import forms
from .models import UserData

class UploadDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['image', 'video']