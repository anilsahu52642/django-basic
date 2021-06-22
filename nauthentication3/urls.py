from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('createobject3/',views.createobject3,name='create_object3'),
path('deleteobject3/<int:id>/',views.deleteobject3,name='delete_object3'),
path('updateobject3/<int:id>/',views.updateobject3,name='update_object3'),
path('createuser3/',views.createuser3,name='create_user3'),
path('signinuser3/',views.signinuser3,name='signin_user3'),
]
