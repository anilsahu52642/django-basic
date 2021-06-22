from django.contrib import admin
from . models import student1,student2
# Register your models here.
@admin.register(student1)
class student1Admin(admin.ModelAdmin):
    list_display=['id','name','roll','city','mark','passdate']


@admin.register(student2)
class student2Admin(admin.ModelAdmin):
    list_display=['id','name','roll','city','mark','passdate','admdate']
