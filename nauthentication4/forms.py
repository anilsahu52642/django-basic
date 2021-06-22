from django import forms
from nauthentication.models import people
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User

class signupuser1(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'password':forms.TextInput(attrs={'class':'form-control'}),'confrom_password':forms.TextInput(attrs={'class':'form-control'})}


class signinuser1(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'password':forms.TextInput(attrs={'class':'form-control'})}


class editform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'


class editform2(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
