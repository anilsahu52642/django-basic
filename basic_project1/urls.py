"""basic_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homeapp.urls')),
    path('',include('timeapp.urls')),
    path('',include('calculatorapp.urls')),
    path('',include('nauthentication.urls')),
    path('',include('nauthentication2.urls')),
    path('',include('nauthentication3.urls')),
    path('',include('nauthentication4.urls')),
    path('',include('cookie.urls')),
    path('',include('cache.urls')),
    path('',include('signalapp.urls')),
    path('',include('middlewares.urls')),
    path('',include('querysetapp.urls')),
    path('',include('modelinheritanse.urls')),
    path('',include('model_relationship.urls')),
    path('',include('class_based_view.urls')),
    path('',include('authentication_view.urls')),
    path('',include('authentication_view.urls')),
    path('',include('pagination.urls')),
    path('',include('image_upload.urls')),
    path('',include('faker_app.urls')),
    path('',include('others.urls')),
    path('',include('real_authentication.urls')),
    path('',include('hostingapp.urls')),
    path('',include('noteapp.urls')),

    ############ for social authentication ##############
    path('oauth/', include('social_django.urls', namespace='social')),






]
