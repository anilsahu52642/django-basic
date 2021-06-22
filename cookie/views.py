from django.shortcuts import render
from datetime import timedelta,datetime
# Create your views here.


#for setting cookies....(see in the browser cookies(google crome-all site and cookies data))
#SETTING COOKIES (Choose any one below method)...
#cookies will stored into browser

# def settingcookies1(request):
#     x=render(request,'cookie/settingcookies1.html')
#     # x.set_cookie('name','anil',max_age=10)
#     x.set_cookie('name','anil',expires=datetime.utcnow()+timedelta(days=2))
#     return x


#for setting signed cookies
#cookies will stored into browser

# def settingcookies1(request):
#     x=render(request,'cookie/settingcookies1.html')
#     x.set_signed_cookie('name','anil',salt='nmm',expires=datetime.utcnow()+timedelta(days=2))
#     return x



#SECTION METHOD(used for saving cookies into database)
def settingcookies1(request):
    request.session['name']='anil'
    # request.session.set_expiry(10)

    return render(request,'cookie/settingcookies1.html')


#for setting test cookies (to check wheather browser cookie enabled or not)

# def settingcookies1(request):
#     request.session.set_test_cookie()
#     print('setting successfully')
#     return render(request,'cookie/settingcookies1.html')



#########################################################################################################################

#GETTING COOKIES (Choose any one below method)...
#here if particular cookies not available then gives error

# def gettingcookies1(request):
#     ck=request.COOKIES['name']
#     return render(request,'cookie/gettingcookies1.html',{'cookie':ck})


#here if particular cookies not found then default value will returned
# def gettingcookies1(request):
#     ck=request.COOKIES.get('name','default value')
#     return render(request,'cookie/gettingcookies1.html',{'cookie':ck})


#for getting signed cookies.....
# def gettingcookies1(request):
#     ck=request.get_signed_cookie('name','default value',salt='nmm')
#     return render(request,'cookie/gettingcookies1.html',{'cookie':ck})

#for getting cookies data from database....
# def gettingcookies1(request):
#     # nm=request.session['name']
#     nm=request.session.get('name','default value from session method')
#     ky=request.session.keys()
#     va=request.session.values()
#     it=request.session.items()
#     ag=request.session.setdefault('age','25')
#     return render(request,'cookie/gettingcookies1.html',{'cookie':nm,'age':ag,'keys':ky,'values':va,'items':it})



#getting test cookie result
# def gettingcookies1(request):
#     res=request.session.test_cookie_worked()
#     return render(request,'cookie/gettingcookies1.html',{'result':res})




#for page count project.........
def gettingcookies1(request):
    pageno=request.session.get('page',default=0)
    pageno=pageno+1
    request.session['page']=pageno
    return render(request,'cookie/gettingcookies1.html',{'pagecount':pageno})

#########################################################################################################################

#FOR DELETING COOKIES ....

#deleting cookies from browser
# def deletecookies1(request):
#     d=render(request,'cookie/deletecookie1.html')
#     d.delete_cookie('name')
#     return d



#deleting cookies from browser......
# def deletecookies1(request):
#     if 'name' in request.session:
#         del request.session['name']
#     return render(request,'cookie/deletecookie1.html')



#for deleting cookies form database
def deletecookies1(request):
    request.session.flush()
    # request.session.clear_expired()
    return render(request,'cookie/deletecookie1.html')



#for deleting test cookies
# def deletecookies1(request):
#     request.session.delete_test_cookie()
#     return render(request,'cookie/deletecookie1.html')





##############################################################################################################
#page counter project
# def pagecount(request):
#     return render(request,'')
