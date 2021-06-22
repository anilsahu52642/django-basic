from django.shortcuts import render,HttpResponseRedirect
from nauthentication.models import people
from django.contrib import messages
from nauthentication2.forms import studentform,studentform2,studentform2signin
from django.contrib.auth.models import User
from django.contrib import auth




#for creating objects in database
def createobject2(request):
    if request.method=='POST':
        x=studentform(request.POST)
        if x.is_valid():
            n=request.POST['mname']
            fn=request.POST['mfname']
            e=request.POST['memail']
            ln=request.POST['mlname']
            p=request.POST['mpassword']
            y=people.objects.create(name=n,password=p,email=e,fname=fn,lname=ln)
            y.save()
            print('success ........')
            messages.info(request,'successfully added..')
            return HttpResponseRedirect('/create2/')
            fm=studentform()

    else:
        fm=studentform()
    return render(request,'nauthentication2/createobject.html',{'form':fm})


#for signup user

def signup2(request):
    if request.method=='POST':
        fm=studentform2(request.POST)
        if fm.is_valid():
            un=request.POST['uname']
            ufn=request.POST['ufname']
            ue=request.POST['uemail']
            uln=request.POST['ulname']
            up=request.POST['upassword']
            x=User.objects.create(username=un,email=ue,first_name=ufn,last_name=uln,password=up)
            x.save()
            print('success 22222')
            messages.info(request,'successfully added..')
            return HttpResponseRedirect('/signup2/')
            fm=studentform2()

    else:
        fm=studentform2()
    return render(request,'nauthentication2/createuser.html',{'form':fm})


#signin user
def signin2(request):
    if request.method=='POST':
        x=studentform2signin(request.POST)
        if x.is_valid():
            signinname=request.POST['usiname']
            signinpassword=request.POST['usipassword']
            y=auth.authenticate(username=signinname,password=signinpassword)
            if y is None:
                messages.error(request,'sorry entered field data are incorrect')
            else:
                messages.success(request,'successfully signed in')
        fm=studentform2signin()
    else:
        fm=studentform2signin()
    return render(request,'nauthentication2/signinuser.html',{'sform':fm})
