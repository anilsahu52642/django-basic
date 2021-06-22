from .models import imageupload2
from django import forms


class imageupload2form(forms.ModelForm):
    class Meta:
        model=imageupload2
        fields=['photo']
        labels={'photo':'Upload your image here'}
