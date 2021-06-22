from django.contrib import admin
from .models import teacher,student3,contractor
# Register your models here.
@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','salary']


@admin.register(student3)
class student3Admin(admin.ModelAdmin):
    list_display=['id','name','age','date','roll']

@admin.register(contractor)
class contractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date']


#######################################################################
##########for proxy model.............
from .models import myexamcenter,examcenter

@admin.register(myexamcenter)
class myexamcenterAdmin(admin.ModelAdmin):
    list_display=['id','centername','centerloc']

@admin.register(examcenter)
class examcenterAdmin(admin.ModelAdmin):
    list_display=['id','centername','centerloc']



############################################################################
##############for multi table inheritance
from .models import animal,creature

@admin.register(creature)
class creatureAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(animal)
class animalAdmin(admin.ModelAdmin):
    list_display=['id','name','legs']
