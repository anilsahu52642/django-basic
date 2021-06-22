from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('settingcookies1/',views.settingcookies1,name='setting_cookies_page'),
path('gettingcookies1/',views.gettingcookies1,name='getting_cookies_page'),
path('deletecookies1/',views.deletecookies1,name='deleting_cookies'),


]
