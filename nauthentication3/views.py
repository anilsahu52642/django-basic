from django.shortcuts import render,HttpResponseRedirect
from nauthentication3.forms import studentform,teacherform,teachersigninform
from nauthentication.models import people
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password

#creating object....
def createobject3(request):
    aobj=people.objects.all()
    if request.method=='POST':
        fm1=studentform(request.POST)
        if fm1.is_valid():
            na1=fm1.cleaned_data['name']
            pa1=fm1.cleaned_data['password']
            e1=fm1.cleaned_data['email']
            fn1=fm1.cleaned_data['fname']
            ln1=fm1.cleaned_data['lname']
            x=people.objects.create(name=na1,password=pa1,email=e1,fname=fn1,lname=ln1)
            x.save()
            print('successfullly added ....')
            messages.success(request,'successfully added....')
            return HttpResponseRedirect('/createobject3/')
    else:
        fm1=studentform()
    return render(request,'nauthentication3/createobject.html',{'form':fm1,'obj':aobj})


#for delete object from database
def deleteobject3(request,id):
    x=people.objects.get(pk=id)
    x.delete()
    return HttpResponseRedirect('/createobject3/')



#for update object of database
def updateobject3(request,id):
    if request.method=='POST':
        x=people.objects.get(pk=id)
        y=studentform(data=request.POST,instance=x)
        if y.is_valid():
            y.save()
            messages.info(request,'successfully updated......,')
            return HttpResponseRedirect('/createobject3/')
    else:
        x=people.objects.get(pk=id)
        y=studentform(instance=x)
        return render(request,'nauthentication3/updateobject.html',{'updateform':y,'oname':x.name})



#for creating users...........
# while creating user if we use (password=password) then after hosting in the website it will authenticate even if after typing correct password and if we go to admin page and see the password then it will show 'invalid-password-format-or-unknown-hashing-algorithm-in-a-custom'...
# so to avoid this type of error use (password=make_password(p)) and import 'make_password'
def createuser3(request):
    if request.method=='POST':
        fm=teacherform(data=request.POST)
        if fm.is_valid():
            n1=fm.cleaned_data['name']
            fn1=fm.cleaned_data['fname']
            ln1=fm.cleaned_data['lname']
            e1=fm.cleaned_data['email']
            p1=fm.cleaned_data['password']
            # x=User.objects.create(username=n1,first_name=fn1,last_name=ln1,email=e1,password=p1)
            x=User.objects.create(username=n1,first_name=fn1,last_name=ln1,email=e1,password=make_password(p1))

            x.save()
            messages.info(request,'Now you can signin......,')
        fm=teacherform()
    else:
        fm=teacherform()
    return render(request,'nauthentication3/createuser.html',{'form':fm})

#for signin user......

def signinuser3(request):
    if request.method=='POST':
        fm=teachersigninform(data=request.POST)
        if fm.is_valid():
            un1=fm.cleaned_data['name']
            up1=fm.cleaned_data['password']
            x=auth.authenticate(username=un1,password=up1)
            if x is None:
                messages.error(request,'sorry username or password is incorrect')
            else:
                messages.success(request,'successfully signed in')
        fm=teachersigninform()
    else:
        fm=teachersigninform()
    return render(request,'nauthentication3/signinuser.html',{'form':fm})
