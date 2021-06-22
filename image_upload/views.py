from django.shortcuts import render
from .forms import uploadform
from .models import image
# Create your views here.


def docupload(request):
    if request.method=='POST':
        aform=uploadform(request.POST,request.FILES)
        if aform.is_valid():
            aform.save()
    else:
        aform=uploadform
    allimage=image.objects.all()
    return render(request,'docupload.html',{'form':aform,'images':allimage})
