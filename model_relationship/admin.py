from django.contrib import admin
from . models import onepage,manypage,song,likethepage
# Register your models here.


@admin.register(onepage)
class onepageAdmin(admin.ModelAdmin):
    list_display=['creater','pagename','pagecatagory']

@admin.register(likethepage)
class likethepageAdmin(admin.ModelAdmin):
    list_display=['page','like']


@admin.register(manypage)
class manypageAdmin(admin.ModelAdmin):
    list_display=['creater','pagename','id','creater_id']

@admin.register(song)
class songAdmin(admin.ModelAdmin):
    list_display=['written','song_name','song_duration']
