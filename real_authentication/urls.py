from django.contrib import admin
from django.urls import path
from . import views as a
from django.contrib.auth import views as b
from .forms import rloginform,myPasswordResetForm
from django.urls import reverse_lazy

urlpatterns=[
    path('admin/',admin.site.urls),
    # path('rlogin/', b.LoginView.as_view(form_class=rlogin,template_name='rlogin.html'), name='reallogin'),
    path('rlogin/',a.rlogin.as_view(),name='reallogin'),
    path('rsignup/', a.rsignup,name='rsignup'),
    path('rprofile/',a.rprofile.as_view(),name='rprofile'),
    # path('rlogout/',a.rlogout.as_view(),name='rlogout'),
    path('rlogout/', b.LogoutView.as_view(template_name='rlogout.html'), name='rlogout'),

    path('rpchange/', a.realpasswordchange.as_view(), name='rpasschange'),
    path('rpchange/done/', a.realpasswordchangedone.as_view(), name='rpasschangedone'),


    path('rpreset/', b.PasswordResetView.as_view(email_template_name = 'preset_email.html',template_name='rpreset.html',success_url='/rpresetdone',form_class=myPasswordResetForm), name='rpreset'),
    path('rpresetdone/', b.PasswordResetDoneView.as_view(template_name='presetdone.html'), name='rpresetdone'),
    path('rpreset/<uidb64>/<token>/', b.PasswordResetConfirmView.as_view(template_name='presetconfirm.html',success_url='/rpreset/done'), name='password_reset_confirm'),
    path('rpreset/done/', b.PasswordResetCompleteView.as_view(template_name='presetcomplete.html'), name='password_reset_complete'),
]
