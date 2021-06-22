from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
path('admin/',admin.site.urls),
path('mid/',views.middleware,name='createmiddleware'),
path('myexception2/',views.exceptioncreate2,name='mexception2'),
path('trmiddleware/',views.templateresponsemiddleware,name='tempresponsemiddleware'),
]
