from django.shortcuts import render,HttpResponse
from signalapp import signals

# Create your views here.

def mysignal(request):
    return render(request,'signal.html')

####for raising error ............
def exceptioncreate(request):
    # print('some error occured')
    a=10/0
    return HttpResponse('this function creates some exception manually')


#####for own customized signal..........

def mycreatedsignal(request):
    signals.mysignal.send(user=['anil','sunil'],request=request,sender=None)
    return HttpResponse('this is for own created customized signals')
