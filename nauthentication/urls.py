from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('signup/',views.signup,name='sign_up'),
path('udelete/<int:id>/',views.deleteuser,name='delete_user'),
path('signin/',views.signin,name='sign_in'),

path('create/',views.createobject,name='create_object'),
path('delete/<int:id>/',views.deleteobject,name='delete_object'),

]
