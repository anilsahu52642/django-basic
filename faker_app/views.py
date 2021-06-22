from django.shortcuts import render

# Create your views here.
def fakedata(request):
    return render(request,'faker_app.html')
