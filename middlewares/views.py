from django.shortcuts import render

# Create your views here.
def middleware(request):
    print('this is for process middleware....from........ views.py..........print')
    return render(request,'middlewares.html')


####for raising error ............
def exceptioncreate2(request):
    a=10/0
    print('some exception occured............from views.py file')
    return HttpResponse('this is for my exception middleware')

#####for templte response middleware.........
from django.template.response import TemplateResponse
def templateresponsemiddleware(request):
    print('this is for template response middleware....from........ views.py..........print')
    context={'name':'anil'}
    return TemplateResponse(request,'middlewares.html',context)
