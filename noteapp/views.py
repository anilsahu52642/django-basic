from django.shortcuts import render,HttpResponseRedirect
from . models import imageupload2
from .forms import imageupload2form
from django.contrib import messages
# Create your views here.
def notes(request):
    if request.method=='POST':
        form=imageupload2form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'uploaded successfully')
    else:
        form=imageupload2form
    allimage=imageupload2.objects.all()
    context={'form':form,'allimage':allimage}
    return render(request,'notes.html',context)


def deletenotes(request,pk):
    imageobject=imageupload2.objects.get(pk=pk)
    imageobject.delete()
    messages.error(request,'file deleted successfully')
    return HttpResponseRedirect('/notes/')