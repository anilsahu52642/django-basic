from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views import View
from .forms import rloginform,rpchangeform
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy

def rsignup(request):
    if request.method=='POST':
        un=request.POST['username']
        ps=request.POST['password']
        x=User(username=un,password=ps)
        x.save()
    return render(request,'rsignup.html')



class rlogin(View):
    def get(self,request):
        fm=rloginform()
        return render(request,'rlogin.html',{'form':fm})
    def post(self,request):
        fm=rloginform(data=request.POST)
        if fm.is_valid():
            u=fm.cleaned_data['username']
            p=fm.cleaned_data['password']
            x=authenticate(username=u,password=p)
            if x!=None:
                login(request,x)
                print('successfull')
                return HttpResponseRedirect('/rprofile/')
            else:
                return HttpResponse('authentication failed')


        return render(request,'rlogin.html',{'form':fm})


class rprofile(TemplateView):
    template_name='rprofile.html'

class rlogout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/rlogin/')


class realpasswordchange(PasswordChangeView):
    template_name='rpchange.html'
    form_class=rpchangeform
    success_url = reverse_lazy('rpasschangedone')

class realpasswordchangedone(PasswordChangeDoneView):
    template_name='rprofile.html'
