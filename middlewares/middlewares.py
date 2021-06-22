from django.shortcuts import HttpResponse


##############for function badsed middleware....................
##########after writing below code we have to register them inside settings.py file-middlewares
##########the middleware which is not required just go to settings.py-middlewares and commment
def mymiddleware1(get_response):
    print('.............................')
    print('code here will executed once when we runserver')
    print('.............................')
    def myfunction(request):
        print('.............................')
        print('code here will allways executed everytime berfore an view function called')
        print('.............................')
        response=get_response(request)
        print('.............................')
        print('code here will allways executed everytime after an view function called')
        print('.............................')
        return response
    return myfunction


##############for class badsed middleware....................



class mymiddleware2:
    def __init__(self1,get_response1):
        self1.get_response2=get_response1
        print('.............................')
        print('code here will executed once when we runserver')
    def __call__(self2,request2):
        print('.............................')
        print('code here will allways executed everytime berfore an view function called')
        # response2=self2.get_response2(request2)
        #######we can pass http response or render also so that response is send from this middleware only without passing to next middleware
        response2=HttpResponse('this is class based middleware')
        print('.............................')
        print('code here will allways executed everytime after an view function called')
        return response2

##########we can give more no of middlewares .................
############mention in the settings.py-middlewares in the order they will executed.....
class anil1:
    def __init__(self1,get_response1):
        self1.get_response2=get_response1
        print('.............................')
        print('one time starting 1')
    def __call__(self2,request2):
        print('.............................')
        print('before view 1')
        response2=self2.get_response2(request2)
        print('.............................')
        print('after view 1')
        return response2
class anil2:
    def __init__(self1,get_response1):
        self1.get_response2=get_response1
        print('.............................')
        print('one time starting 2')
    def __call__(self2,request2):
        print('.............................')
        print('before view 2')
        response2=self2.get_response2(request2)
        print('.............................')
        print('after view 2')
        return response2
class anil3:
    def __init__(self1,get_response1):
        self1.get_response2=get_response1
        print('.............................')
        print('one time starting 3')
    def __call__(self2,request2):
        print('.............................')
        print('before view 3')
        response2=self2.get_response2(request2)
        print('.............................')
        print('after view 3')
        return response2



################we can pass some extra function to middleware............

#######For process middleware............
class processmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('.............................')
        print('one time starting')
    def __call__(self,request):
        print('.............................')
        print('before view')
        response=self.get_response(request)
        print('.............................')
        print('after view')
        return response
#########here process_view is fixed no own given name allowed...write as like below
    def process_view(request,*args,**kwargs):
        print('.............................')
        print('before process view')
#######if it returns None it takes output from views.py file,,,if it returns TemplaResponse then it shows output from views.py file
        return HttpResponse('this is from process middleware')
        # return None


#######For exception middleware............
class myexceptionmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('.............................')
        print('one time starting')
    def __call__(self,request):
        print('.............................')
        print('before view')
        response=self.get_response(request)
        print('.............................')
        print('after view')
        return response
    def process_exception(self,request,exception):
        print('.............................')
        print('before exception view')
        msg=exception
        print('exception:',msg)
        print('class of exception:',exception.__class__.__name__)
        # return HttpResponse('this is from exception middleware')
        return None


#########go to views.py file and give exception.......



#######For template response middleware............
class mytemplateresponsemiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('.............................')
        print('one time starting')
    def __call__(self,request):
        print('.............................')
        print('before view')
        response=self.get_response(request)
        print('.............................')
        print('after view')
        return response
    def process_template_response(self,request,response):
        print('.............................')
        print('before template response view')
        response.context_data['name']='sunil'
        return response




############################################################################################################
############################################################################################################
#########for site not working or site under construction project...........
from django.shortcuts import render

class siteunderconstructionmiddleware:
    def __init__(self1,get_response1):
        self1.get_response2=get_response1
    def __call__(self2,request2):
        # response2=HttpResponse('this site is under construction ...please try again later.....')
        response2=render(request2,"construction.html")
        return response2
