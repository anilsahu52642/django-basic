from nauthentication.models import people
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model=people
        fields=['name','fname','lname','email','password']
        labels={'fname':'First Name','lname':'Last Name'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'fname':forms.TextInput(attrs={'class':'form-control'}),'lname':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'password':forms.TextInput(attrs={'class':'form-control'})}
        help_text={'name':'enter name','fname':'enter first name'}


class teacherform(forms.ModelForm):
    class Meta:
        model=people
        fields=['name','email','fname','lname','password']
        labels={'name':'username','fname':'first Name','lname':'Last Name'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'fname':forms.TextInput(attrs={'class':'form-control'}),'lname':forms.TextInput(attrs={'class':'form-control'}),'password':forms.TextInput(attrs={'class':'form-control'})}


class teachersigninform(forms.ModelForm):
    class Meta:
        model=people
        fields=['name','password']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'password':forms.TextInput(attrs={'class':'form-control'})}
