from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from nauthentication.models import people
from django.contrib import messages
from django.contrib import auth
# Create your views here.
#creating user(signup,signin...) using models type1 and print in browser
def signup(request):
    if request.method=='POST':
        n1=request.POST['uname1']
        p1=request.POST['upassword1']
        e1=request.POST['uemail1']
        fn1=request.POST['funame1']
        ln1=request.POST['luname1']
        print('success 1')
        c=User.objects.create_user(username=n1,email=e1,first_name=fn1,last_name=ln1,password=p1)
        print('success 2')
        c.save()
        print('created successfully')
        us=User.objects.all()
    else:
        us=User.objects.all()
    return render(request,'nauthentication/createuser.html',{'alluser':us})

#delete user from database..
def deleteuser(request,id):
    x=User.objects.get(pk=id)
    x.delete()
    return HttpResponseRedirect('/signup/')

#update user of database from frontend(not working in this type search form browser)



#for signin user
def signin(request):
    if request.method=='POST':
        n1=request.POST['usname1']
        p1=request.POST['uspassword1']
        a=auth.authenticate(username=n1,password=p1)
        if a is None:
            print('sorry canot signin')
            return HttpResponseRedirect('/signin/')

        else:
            print('successfully signed in')
        return HttpResponseRedirect('/signup/')
    else:
        print('first signin')
    return render(request,'nauthentication/signinuser.html')


#creating objects to database using models and view in page
def createobject(request):
    if request.method=='POST':
        n=request.POST['name2']
        p1=request.POST['password1']
        p2=request.POST['password2']
        e2=request.POST['email2']
        fn2=request.POST['fname2']
        ln2=request.POST['lname2']
        x=people.objects.create(name=n,password=p1,password2=p2,email=e2,fname=fn2,lname=ln2)
        x.save()
        print('successfully saved')
        return HttpResponseRedirect('/create/')
    else:
        cr=people.objects.all()
        print(cr)
        return render(request,'nauthentication/createobject.html',{'allobjects':cr})
#for delete objects from database
def deleteobject(request,id):
    y=people.objects.get(pk=id)
    y.delete()
    cr=people.objects.all()
    return HttpResponseRedirect('/create/')


#for updating database data of ojects..(im my program it is not updating creating a new entry)
