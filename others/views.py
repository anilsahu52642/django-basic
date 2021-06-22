from django.shortcuts import render

# Create your views here.
def other1(request):
    return render(request,'rough.html')


def other2(request):
    return render(request,'rough2.html')
