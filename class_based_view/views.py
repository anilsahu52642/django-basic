from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import student10


# Create your views here.
class myview1(View):
    name2='anil2'
    def get(self,request):
        name='anil'
        context={'myname':name,'myname2':self.name2}
        return render(request,'class_based_view/view1.html',context)


########################################
class myview2(myview1):
    def get(self,request):
        return render(request,'class_based_view/view1.html',{'myname2':self.name2})


#########################################
class myview3(View):
    def get(self,request):
        form=student10
        return render(request,'class_based_view/view1.html',{'form':form})
    def post(self,request):
        form=student10(request.POST)
        if form.is_valid():
            print('email:',form.cleaned_data['email'])
        return HttpResponse('form submtted......successfully')


#########################################



#######################additional for function based view
def fview(request,templatename):
    templatename='class_based_view/view1.html'
    return render(request,templatename)



##############################################################
class myview4(View):
    templatename=''
    def get(self,request):
        return render(request,self.templatename)





######################################################################################
#################for template view (only import statement required).....
from django.views.generic.base import TemplateView


####################for defining template name inside views.py file without urls.py
class tempview2(TemplateView):
    template_name='class_based_view/view2.html'
    ############for passing context data........
    def get_context_data(self,**kwargs):
        acontext=super().get_context_data(**kwargs)
        acontext['name']='anil'
        acontext['surname']='sahu'
        # acontext={'name':'anil','surname':'sahu'}
        ##########for passing extra context data..........extra context data is given inside urls.py file
        ###########for print what is inside **kwargs............
        # print('kwargs data:',**kwargs)
        return acontext

##################################################################################
##########for redirect view(only import statement required)

from django.views.generic.base import RedirectView

#################for defining url inside views.py file .............
class redirectview2(RedirectView):
    # url='http://youtube.com'
    ##########here inside this url path should be given
    # url='/tv2/'
    #############for pattern name inside views.py file...............
    pattern_name='tview2'
    #########for changing status code from 302 to 301 during redirect(see in the terminal)(default=302)
    permanent=True
    ##########for changing query string..............http://127.0.0.1:8000/tv2/?kaklajdkhkaladddlaa   (after ? all typed text is query string)
    # query_string=True
    ###############for passing extra methods......
    def get_redirect_url(self,*args,**kwargs):
        print(kwargs)
        kwargs['aaks']=12345
        return super().get_redirect_url(*args,**kwargs)





##################################################################################################################
#########for generic view........(display view,edit view,edit view,date view)
#########for display view(lisplay view)(used for displaying all objects of data base model)
from django.views.generic.list import ListView
from nauthentication.models import people

class peopledetail1(ListView):
    model=people
    ############for own template suffix name(default is list...people_list.html).......because of below line the template name should be people_anil.html
    # template_name_suffix='_anil'
    ###########for own template name and location...........
    template_name='class_based_view/view3.html'
    #################for changing context name(here default is modelname_list  ...used in html file to access element of database object)...because of below line we have to use {% for s in 123peoplesss %} in template file....
    context_object_name='123peoplesss'
    #################for getting some of the data of batabase..........
    def get_queryset(self):
        return people.objects.filter(email='anil.sipun52642@gmail.com').order_by('id').reverse()
    ##################we can pass some other functionality like if name...anil is available in cookie then show one page otherwise another page
    # def get_template_name(self):
    #     if self.request.COOKIE['name']=='anil':
    #         template_name='a.html'
    #     else:
    #         template_name=self.template_name
    #
    #     return [template_name]

    ##############some other functionality.......
    # def get_template_name(self):
    #     if self.request.user.is_super_user:
    #         tempate_name='a.html'
    #     elif self.request.user.is_staff:
    #         template_name='b.html'
    #     else:
    #         template_name=self.template_name
    #
    #     return [template_name]




###########################################################################################
##############for detail view...........(for viewing data of particular object ...)so in urls.py file we have to give pk....
from django.views.generic.detail import DetailView
from nauthentication.models import people

class peopledetailview(DetailView):
    model=people
    tempate_name='class_based_view/view3.html'
    #########default context object name is modelname...(people)....by using below line context_object_name is apeople .....use in html file to show object in browser
    context_object_name='apeople'
    ##########for above program we have to use (pk)....if we want to use another name....  write code inside views.py file....(so that we can use in html file or to print kwargs data use function)
    ###### pk_url_kwargs='dog'



#############################################################################################
###########for generic editting view(form view,create view,delete view,update view)

#############for form view..........(for displaying form and validating form data...)
from .forms import student10
from django.views.generic.edit import FormView,CreateView



class studentform7(FormView):
    form_class=student10
    ###########after we click submit in browser where we have to go we have to define.....by success_url
    success_url='/thankyou/'
    ###########for giving intial value to form ...........
    initial={'name':'anil','email':'anilsahu@gmail.com'}
    ###########for catching form data and validating form data ........................
    def form_valid(self,form):
        print('form is valid')
        print(form.cleaned_data['name'])
        # return super().form_valid(form)
        #######we can render some page........
        return HttpResponse('form data are valid')

#######################################################################################
###########for create view(used for creating user and creating object in database....and showing form validating form)
from django.views.generic.edit import CreateView


# from django import forms
# class studentform8(CreateView):
#     model=people
#     fields=['name','email','fname','lname','password']
#     #######we can give default template name or can give our own template.....(tempalte name is given in urls.py file)
#     success_url='/thankyou/'
#     ################for giving bootstrap class or other class...........
#     def get_form(self):
#         form=super().get_form()
#         form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
#         form.fields['email'].widget=forms.EmailInput(attrs={'class':'myclass'})
#         form.fields['password'].widget=forms.PasswordInput(attrs={'class':'myclass'})
#         return form
#
####################for creatin user in the data base.........................
from django.contrib.auth.models import User
from django import forms
class studentform8(CreateView):
    model=User
    fields=['username','email','first_name','last_name','password']
    success_url='/thankyou/'


#############for giving bootstrap class we can use model form and import here
from django.views.generic.edit import CreateView
from .forms import student11


class studentform9(CreateView):
    model=student11
    fields=['name','fname','lname','email','password']
    success_url='/thankyou/'



###############################################################################################
#########for update view (for updating one particular object data or user data).........here inside url pk is required.......for user just metion model=User and give its fields
from django.views.generic.edit import UpdateView
class studentform12(UpdateView):
    model=people
    fields=['name','email','fname','lname','password']
    success_url='/thankyou/'
    ################for giving bootstrap class or other class...........
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(render_value=True,attrs={'class':'myclass'})
        return form
        ###########here for above program when we use bootstrap class or any class during update view then in password field no previous password is visible ... to make it visible mention render_value=True in the passeord as like above line or we can give inside forms.py fie if we are using modle form



##########################################################################################
#############for delete view.....(for delete one user or object from database)............here we have to give pk inside urls.py file....for user just metion model=User and give its fields
#################in this view after hitting url it will takes into conform page where we have to click conform after that it will delete the object
from django.views.generic.edit import DeleteView

class studentform13(DeleteView):
    model=people
    success_url='/thankyou/'
