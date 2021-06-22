from django import forms
from .models import image


class uploadform(forms.ModelForm):
    class Meta:
        model=image
        fields=['photo']
        labels={'photo':''}

########### as time and date are automatically added we not have to give fields inside form.....if we give then error...
