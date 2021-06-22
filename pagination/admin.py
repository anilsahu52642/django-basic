from django.contrib import admin

# Register your models here.
from .models import blog

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display=['id','writer','content']
