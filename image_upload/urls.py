from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',views.docupload,name='docupload'),

    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#######code is written in upper written program......by these code django can find the path to see media files
