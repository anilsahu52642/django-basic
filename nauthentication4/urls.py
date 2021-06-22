from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('fcreateuser/',views.fcreateuser,name='full_user_form'),
path('usercreate4/',views.createuser4,name='ncreate_user4'),
path('signinuser4/',views.signinuser4,name='signin_user4'),
path('profile4/',views.profile4,name='profile_page4'),
path('userlogout/',views.userlogout,name='logout_page'),
path('passwordchange1/',views.passwordchange1,name='password_change1'),
path('passwordchange2/',views.passwordchange2,name='password_change2'),

]
