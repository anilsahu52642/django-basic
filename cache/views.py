from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

#This is per site caching.........
# @cache_page(15)
# def cache1(request):
#     return render(request,'cache/cache1.html')
#
#
# @cache_page(15)
# def cache2(request):
#     return render(request,'cache/cache2.html')


################################################################################################################
#this is per view caching........


# def cache1(request):
#     return render(request,'cache/cache1.html')
#
# def cache2(request):
#     return render(request,'cache/cache2.html')





################################################################################################################
#this is template fragment caching........
######some code are written in template file..........

def cache1(request):
    return render(request,'cache/tempcache1.html')




################################################################################################################

##########this is for deleting cache from database......
##############not working see see again from video ..............cache is not defined   error

def delete(request):
    cache.delete('name')
    cache.delete('name',version=2)
    #cache.clear()
    return render(request,'cache/delete.html')
