#In this type form form creation no html code written only forms.py



from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('create2/',views.createobject2,name='create_object2'),
path('signup2/',views.signup2,name='signup_user2'),
path('signin2/',views.signin2,name='signin_user2'),
]
