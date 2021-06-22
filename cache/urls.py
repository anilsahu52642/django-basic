from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


#for per site caching.........
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cache1/',views.cache1,name='cache_page1'),
#     path('cache2/',views.cache2,name='cache_page2'),
# ]
######################################################################
#for per view caching.........
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cache1/',cache_page(15)(views.cache1),name='cache_page1'),
#     path('cache2/',views.cache2,name='cache_page2'),
# ]


######################################################################

#for template fragment caching.....
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cache1/',views.cache1,name='cache_page1'),
    path('delcache/',views.delete,name='deletecache'),

]




########################################################################
#########for delete cahce............
