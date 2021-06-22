from django.shortcuts import render
import datetime
# Create your views here.
def time(request):
    d=datetime.datetime.now()
    print(d)
    h=int(d.strftime('%H'))
    wish='hello...'
    if h<10:
        wish=wish+'Good morning'
    elif h<15:
        wish=wish+'Good afternoon'
    elif h<20:
        wish=wish+'Good enening'
    else:
        wish=wish+'Good night'
    return render(request,'datetime.html',{'msg':wish,'dt':d})
