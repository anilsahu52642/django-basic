from django.shortcuts import render
from .models import teacher,student3,contractor
# Create your views here.
def modelinheritance(request):

    # ###########for default manager ................here manager is objects........
    # data1=teacher.objects.all()
    # data2=student3.objects.all()
    # data3=contractor.objects.all()

    ###########for our own  manager name ................here manager is anil1,anil2,anil3........
    # data1=teacher.anil1.all()
    # data2=student3.anil2.all()
    # data3=contractor.anil3.all()

    ###########for customized manager ................here manager is anil4,anil5,anil6 ........(code written in managers.py file and mention the class name in models.py)
    data1=teacher.anil4.all()
    data2=student3.anil5.all()
    data3=contractor.anil6.all()


    context={'tdata':data1,'sdata':data2,'cdata':data3}
    return render(request,'modelinheritance.html',context)
