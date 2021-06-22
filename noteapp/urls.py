from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('admin/',admin.site.urls),
    path('notes/',views.notes,name='notes'),
    path('deletenotes/<int:pk>/',views.deletenotes,name='deletenotes'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
