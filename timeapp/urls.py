from django.contrib import admin
from django.urls import path
from timeapp import views
urlpatterns=[
path('admin/',admin.site.urls),
path('time/',views.time,name='date_and_time'),
]
