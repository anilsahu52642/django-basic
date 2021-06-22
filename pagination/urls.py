from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #######for function based view.....
    # path('page', views.pageno,name='pagenumbering'),
    #######for class based view.........
    path('page/', views.pageno.as_view(),name='pagenumbering'),
    path('apage/<int:pk>/', views.fulldeatil.as_view(),name='fulldeatil'),


    ]
