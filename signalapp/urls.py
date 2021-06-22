from django.contrib import admin
from django.urls import path
from .import views
urlpatterns=[
path('admin/',admin.site.urls),
path('signal/',views.mysignal,name='signal_page'),
path('myexception/',views.exceptioncreate,name='mexception'),
path('ocsignal/',views.mycreatedsignal,name='customizedsignals'),
]
