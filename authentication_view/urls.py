from django.contrib import admin
from django.urls import path,include
from . import views as a
from django.contrib.auth import views as b
from .forms import pchangeform

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth1/',a.authentication1,name='authentication1'),
    #############all codes are written inside django just we have to import and call this functions.....no need to write inside views.py file
    ########here because of below line if we hit http://127.0.0.1:8000/auth1/login/   then access login funciton and similar for other
    #################it will show error page and show default template name for this....registration/login.html    create it...and create a form
    path('auth1/',include('django.contrib.auth.urls')),
    ###########after login success by default it will go to url http://127.0.0.1:8000/accounts/profile/  so crete url and views for profile
    path('accounts/profile/',a.profilepage111,name='profilepage111'),
    ############for logout ..http://127.0.0.1:8000/auth1/logout/
    #############for password change.......http://127.0.0.1:8000/auth1/password_change      enter url after going to profile page otherwise error
    ###########after successful passoword change done by default it goes to http://127.0.0.1:8000/auth1/password_change/done/
    ###########for password reset .....http://127.0.0.1:8000/auth1/password_reset/.......after hitting this url we will redirect to page where it ask for enter email id for sending message to mail for reset password.........but as we are in developer mode so it will not send mail...so we have to write some code for backend mail so that it will give a link to password reset in terminal..........(see settings.py file)
    ############after this it will send a link to terminal (consol) and goesto page http://127.0.0.1:8000/auth1/password_reset/done/ .........we can reset password by going to link given in the terminal
    ###########after login by default it goes to page http://127.0.0.1:8000/accounts/profile/  to change it mention in the settings.py file    in  LOGIN_REDIRECT_URL
    ########for login required......... if user is not logged in try to access profile page then it will go to page  http://127.0.0.1:8000/accounts/login/?next=/accounts/profile/......here it will give error as we have no url for this so.....to avoid this we can give in urls inside path(in include line of applevel) instead  of auth1  give account
    ##############here we are logged in or not if we are hitting url for http://127.0.0.1:8000/accounts/profile/    then it will go to profile page so if want to show the page if use is logged in....then go to views.py file and give login required...............similarly we can show a page if user is a staff by using staff_member_required inside views.py file



    #####################################################################################################################
    ###########for class based view.....................................

    ############# for implimenting login required and staff_member_required we can write code inside urls.py file or views.py file for class based view
    ############# here code is written inside views.py file..........
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/profile2/',a.profilepage222.as_view(),name='profilepage222'),


    ############# for implimenting login required and staff_member_required we can write code inside urls.py file or views.py file for class based view
    ############# here code is written inside urls.py file..........

    # path('accounts/profile2/',login_required(a.profilepage222.as_view()),name='profilepage222'),
    # path('accounts/profile2/',staff_member_required(a.profilepage222.as_view()),name='profilepage222'),


    ########customising full authentication form.............

    ##########If we are using above codes then after succcessful password reset and other similar like that we are redirecting to the django's default template to change it we can customise it....
    path('custom/',include('django.contrib.auth.urls')),
    # path('login33333/', b.LoginView.as_view(template_name='authentication_view/auth2.html'), name='login33333'),
    path('login33333/', a.customlogin1.as_view(), name='login33333'),

    path('profile33333/',a.TemplateView.as_view(template_name='authentication_view/profile111.html'),name='cprofile3'),

    path('logout33333/',b.LogoutView.as_view(template_name='authentication_view/auth1.html'),name='logout33333'),
    path('pchange33333/',b.PasswordChangeView.as_view(template_name='authentication_view/pchange33333.html',form_class = pchangeform,success_url='/pchangedone33333/'),name='pchangepage33333'),
    #########after successfull password change or reset give success url inside path of password change or password reset......see above line code........
    path('pchangedone33333/',b.PasswordChangeDoneView.as_view(template_name='authentication_view/success33333.html'),name='pchangedone33333'),

    ]
