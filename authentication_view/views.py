from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def authentication1(request):
    return render(request,'authentication_view/auth1.html')

##############here we are logged in or not if we are hitting url for http://127.0.0.1:8000/accounts/profile/    then it will go to profile page so if want to show the page if use is logged in....then

########for login required......... if user is not logged in try to access profile page then it will go to page  http://127.0.0.1:8000/accounts/login/?next=/accounts/profile/......here it will give error as we have no url for this so.....to avoid this we can give in urls inside path(in include line of applevel) instead  of auth1  give account
# @login_required
##########for staff member required ....show a page if use is a staff ..........if use is not a staff want to access a page then it will redirect to admin page to change staff status
# @staff_member_required
@login_required
def profilepage111(request):
    return render(request,'authentication_view/profile111.html')



################################################################################################################
############for class based view.........................................

############# for implimenting login required and staff_member_required we can write code inside urls.py file or views.py file for class based view
############# here code is written inside urls.py file..........

# from django.views import View
# class profilepage222(View):
#     def get(self,request):
#         tname='authentication_view/profile111.html'
#         return render(request,tname)



############# here code is written inside views.py file..........
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.views import View


@method_decorator(staff_member_required,name='dispatch')
class profilepage222(View):
    def get(self,request):
        tname='authentication_view/profile111.html'
        return render(request,tname)





########customising full authentication form.............

##########If we are using above codes then after succcessful password reset and other similar like that we are redirecting to the django's default template to change it we can customise it....
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import customloginform


class customlogin1(LoginView):
    template_name='authentication_view/auth2.html'
    form_class=customloginform
    # authentication_form=customloginform
    
