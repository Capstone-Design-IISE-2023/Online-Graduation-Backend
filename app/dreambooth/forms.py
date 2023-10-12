from django import forms
from .models import UserPhotos

class UserImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserPhotos
        fields = ['image']