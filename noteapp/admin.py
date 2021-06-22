from django.contrib import admin

# Register your models here.
from .models import imageupload2

@admin.register(imageupload2)
class imageupload2Admin(admin.ModelAdmin):
    list_display=['id','photo','date']