from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('admin/',admin.site.urls),
path('calc/',views.calculateit,name='mini_calculator'),
]
