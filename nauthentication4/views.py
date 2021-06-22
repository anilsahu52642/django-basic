from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from nauthentication4.forms import signupuser1,signinuser1,editform,editform2
from django.contrib import messages
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib import auth
from django.contrib.auth.models import Group
# Create your views here.


#full user creation,user change,password change,password setting form
#for required field we can inherite these forms in forms.py
def fcreateuser(request):
    fm1=UserCreationForm()
    fm2=UserChangeForm()
    fm3=AuthenticationForm()
    fm4=PasswordChangeForm(user=request.user)
    fm5=SetPasswordForm(user=request.user)
    return render(request,'nauthentication4/fulluserform.html',{'form1':fm1,'form2':fm2,'form3':fm3,'form4':fm4,'form5':fm5})

#user signup
#to use below code replce the code with below createuse4...(otherwist comment alernetly)
def createuser4(request):
    if request.method=='POST':
        fm=signupuser1(data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'successfully create user... now you can login')
    else:
        fm=signupuser1()
    return render(request,'nauthentication4/createuser.html',{'form':fm})


#creating and adding user into some group from browser...
#to use below code replce the code with above createuse4...(otherwist comment alernetly)
# def createuser4(request):
#     if request.method=='POST':
#         fm=signupuser1(data=request.POST)
#         if fm.is_valid():
#             x=fm.save()
#             gp=Group.objects.get(name='teacher')
#             x.groups.add(gp)
#
#             messages.success(request,'successfully create user... now you can login')
#     else:
#         fm=signupuser1()
#     return render(request,'nauthentication4/createuser.html',{'form':fm})
#
#
#

#for signin user
def signinuser4(request):
    if request.method=='POST':
        fm=signinuser1(data=request.POST)
        if fm.is_valid():
            n=fm.cleaned_data['username']
            p=fm.cleaned_data['password']
            x=auth.authenticate(username=n,password=p)
            if x is None:
                messages.error(request,'sorry some fiels are incorrect..')
            else:
                login(request,x)
                return HttpResponseRedirect('/profile4/')
    else:
        fm=signinuser1()
    return render(request,'nauthentication4/signinuser4.html',{'form':fm})


#for login user
def profile4(request):
    if request.method=='POST':
        anil=editform2(data=request.POST,instance=request.user)
        if anil.is_valid():
            anil.save()
            return HttpResponseRedirect('/profile4/')
            # return render(request,'nauthentication4/profile.html',{'form':anil})
    else:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if request.method=='POST':
                    anil=editform(instance=request.user,data=request.POST)
                    anil.save()
                else:
                    anil = editform(instance=request.user)

            else:
                anil=editform2(instance=request.user)
            return render(request,'nauthentication4/profile.html',{'form':anil})
        else:
            return HttpResponseRedirect('/signinuser4/')


#for logout user
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/signinuser4/')

#for changing password when old password is known...
def passwordchange1(request):
    if request.method=='POST':
        x=PasswordChangeForm(user=request.user,data=request.POST)
        if x.is_valid():
            x.save()
            update_session_auth_hash(request,x.user)
            return HttpResponseRedirect('/profile4/')
    else:
        x=PasswordChangeForm(user=request.user)
        return render(request,'nauthentication4/passwordchange1.html',{'pform':x})


#changing password when previous password is not known....
def passwordchange2(request):
    if request.method=='POST':
        y=SetPasswordForm(user=request.user,data=request.POST)
        if y.is_valid():
            y.save()
            update_session_auth_hash(request,y.user)
            return HttpResponseRedirect('/profile4/')
    else:
        fm2=SetPasswordForm(user=request.user)
    return render(request,'nauthentication4/passwordchange2.html',{'form2':fm2})
