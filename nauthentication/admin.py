from django.contrib import admin

# Register your models here.
from nauthentication.models import people
@admin.register(people)
class peopleAdmin(admin.ModelAdmin):
    list_display=['id','name','password','password2','email','fname','lname']
    
