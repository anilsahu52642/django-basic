from django import forms

class studentform(forms.Form):
    mname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),initial='anil',label='Sweet_Name')
    mpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),empty_value='sahusahu')
    memail=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),help_text='Enter your email here',label_suffix='anil')
    mfname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),min_length=4,max_length=10,strip=False)
    mlname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your surname'}),empty_value='sahu')


class studentform2(forms.Form):
    uname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),label='name')
    upassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}),label='password')
    uemail=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}),label='email')
    ufname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'}),label='first name')
    ulname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter last last name'}),label='last name')


class studentform2signin(forms.Form):
    usiname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),label='name')
    usipassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}),label='password')
