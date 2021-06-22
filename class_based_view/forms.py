from django import forms
class student10(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()



########################################################################
from nauthentication.models import people

class student11(forms.ModelForm):
    class Meta:
        fields=['name','fname','lname','email','password']
        widgets={'name':forms.TextInput(attrs={'class':'myclass'}),
        'password':forms.PasswordInput(attrs={'class':'myclass'}),

        }
