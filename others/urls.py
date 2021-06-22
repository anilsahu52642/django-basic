from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('other/',views.other1,name='other'),
path('other2/',views.other2,name='other2'),

]
