from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
from .models import blog
from django.http import Http404


class pageno(ListView):
    model=blog
    template_name='pagination/page1.html'
    ordering=['id']
    paginate_by=3
    paginate_orphans=2
    def get_context_data(self,*args,**kwargs):
        try:
            return super(pageno,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(pageno,self).get_context_data(*args,**kwargs)



class fulldeatil(DetailView):
    model=blog
    template_name='pagination/page1.html'
