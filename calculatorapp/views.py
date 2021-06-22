from django.shortcuts import render

# Create your views here.
def calculateit(request):
    if request.method=='POST':
        a=int(request.POST['first'])
        b=int(request.POST['second'])
        c=a+b
        return render(request,'calculator.html',{'value':c})
    return render(request,'calculator.html')
