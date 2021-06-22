from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mv1/',views.myview1.as_view(name2='sunil'),name='myview1'),
    path('mv2/',views.myview2.as_view(),name='myview2'),
    path('mv3/',views.myview3.as_view(),name='myview3'),

    path('fv/',views.fview,{'templatename':'class_based_view/view1.html'},name='fview1'),

    path('mv4/',views.myview4.as_view(templatename='class_based_view/view1.html'),name='myview4'),


    ###############for templateview..................................................
    path('tv1/',views.TemplateView.as_view(template_name='class_based_view/view1.html'),name='tview1'),
    # ####################for defining template name inside views.py file without urls.py
    path('tv2/',views.tempview2.as_view(),name='tview2'),
    # ##############for passing extra context data........
    path('tv3/',views.tempview2.as_view(extra_context={'roll':'23'}),name='tview3'),
    # ###########for print what is inside **kwargs............
    path('tv4/<int:aks>/',views.tempview2.as_view(),name='tview4'),
    #################we can use slug field also..........
    path('tv5/<slug:post>/',views.TemplateView.as_view(template_name='class_based_view/view1.html'),name='tview5'),

    ###############for redirect view..................................................
    ##########here inside url we have to give url path only no url name willl work
    path('rd1/',views.RedirectView.as_view(url='/tv2/'),name='redview1'),
    ################for defining url inside views.py file with out in urls.py  file......
    path('rd2/',views.redirectview2.as_view(),name='redview2'),
    ##################for redirect using pattern name........
    path('rd3/',views.RedirectView.as_view(pattern_name='tview2'),name='redview3'),
    #############for pattern name inside views.py file.........
    path('rd4/',views.redirectview2.as_view(),name='redview4'),


    ##################for list view....................................................
    ##########by using default template name
    path('lv1/',views.peopledetail1.as_view(template_name='nauthentication/people_list.html'),name='listview1'),
    ##########by using own template name
    path('lv2/',views.peopledetail1.as_view(),name='listview2'),
    #############for detail view......................................................
    path('dv1/<int:pk>/',views.peopledetailview.as_view(template_name='nauthentication/people_detail.html'),name='detailview1'),
    ##########if we use default template name ...nauthentication/people_detail.html otherwise use own template name as like previous
    ##########for own created template file..........................
    path('dv2/<int:pk>/',views.peopledetailview.as_view(template_name='class_based_view/view3.html'),name='detailview2'),
    ##########in above program we have to use (pk)....if we want to use another name....  write code inside views.py file
    ########path('dv3/<int:dog>/',views.peopledetailview.as_view(template_name='class_based_view/view3.html'),name='detailview3'),


    ##################for form view....................................................
    path('fv2/',views.studentform7.as_view(template_name='class_based_view/view4.html'),name='formview2'),
    ###########after we click submit in browser where we have to go we have to define.....by success_url
    path('thankyou/',views.TemplateView.as_view(template_name='class_based_view/thankyou.html'),name='thankyoupage'),




    #####################for update view...................................
    path('cv2/',views.studentform8.as_view(template_name='class_based_view/view4.html'),name='createview2'),
    path('cv3/',views.studentform9.as_view(template_name='class_based_view/view4.html'),name='createview3'),

    ########################for update view...................................
    path('uv1/<int:pk>/',views.studentform12.as_view(template_name='class_based_view/view4.html'),name='updateview1'),


    #####################for update view...................................
    #################in this view after hitting url it will takes into conform page where we have to click conform after that it will delete the object
    path('delv1/<int:pk>/',views.studentform13.as_view(template_name='class_based_view/view4.html'),name='deleteview1'),



]
