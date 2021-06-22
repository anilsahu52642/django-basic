from django.shortcuts import render
from .models import student1,student2
from django.db.models import Q,Avg,Sum,Max,Min,Count
from datetime import datetime,date,time


# Create your views here.
def myqueryset(request):
    # data=student1.objects.all()
    # data=student1.objects.filter(name='rupesh')
    # data=student1.objects.filter(passdate='2020-08-29')
    # data=student1.objects.all().order_by('name')
    # data=student1.objects.all().order_by('passdate').reverse()
    # data=student1.objects.all().order_by('city').reverse()[:3]
    # data=student1.objects.values()
    # data=student1.objects.values_list()
    # data=student1.objects.values_list('name','roll')
    # data=student1.objects.values_list('name','roll',named=True)
    # data=student1.objects.using('default')
    # data=student1.objects.dates('passdate','month')
    # data=student1.objects.dates('passdate','year')




    # data1=student1.objects.values_list('name','roll','city',named=True)
    # data2=student2.objects.values_list('name','roll','city',named=True)
    # data=data1.union(data2)
    # data=data1.union(data2,all=True)
    # data=data1.intersection(data2)


    # data=student1.objects.filter(name='kajal')&student1.objects.filter(mark=68)
    # data=student2.objects.filter(city='kashmir',id=4)
    # data=student1.objects.filter(Q(id=3)&Q(name='rupesh'))
    # data=student1.objects.filter(name='kajal')|student1.objects.filter(mark=37)
    # data=student1.objects.filter(Q(id=3)|Q(name='rupesh'))
    data=student1.objects.all()



    detail=student1.objects.get(pk=1)
    # detail=student1.objects.filter(name='kajal')
    # detail=student1.objects.order_by('id')
    # detail=student1.objects.first()
    # detail=student1.objects.last()
    # detail=student1.objects.latest('name')
    # detail=student1.objects.latest('passdate')
    # detail=student1.objects.earliest('name')
    # detail=student1.objects.earliest('passdate')

##############################################################################
######for crating,updating,deleting   object in database....
    # detail=student1.objects.create(name='anasuya',roll=107,city='khordha',mark=74,passdate='2018-12-23')
    # detail=student1.objects.get_or_create(name='kalyani',roll=108,city='muradabad',mark=24,passdate='2017-02-28')
    # somedata=[student1(name='sahid',roll=114,city='bihar',mark=54,passdate='2020-12-23'),student1(name='priyanka',roll=115,city='utterpradesh',mark=48,passdate='2020-12-2'),student1(name='mike',roll=116,city='westbengal',mark=95,passdate='2020-1-23')]
    # detail=student1.objects.bulk_create(somedata)


    # detail=student1.objects.filter(name='mike').update(name='manisha')
    # detail=student1.objects.update_or_create(name='priyanka',defaults={'name':'priya'})
    # data1=student1.objects.filter(name='sameer')
    # for m in data1:
    #     m.mark=47
    # detail=student1.objects.bulk_update(data1,['mark'])


    # detail=student1.objects.filter(roll=107).delete()
    # detail=student1.objects.filter(pk=18).delete()


    detail=student1.objects.all()

    # data2=student1.objects.in_bulk([])
    # data2=student1.objects.in_bulk()
    # data2=student1.objects.in_bulk([1,2,3])
    # print(data2[3].name)


    # data=student2.objects.filter(name='hrithik')
    # data=student2.objects.filter(name__exact='hrithik')
    # data=student2.objects.filter(name__iexact='hrithik')
    # data=student2.objects.filter(name__startswith='a')
    # data=student2.objects.filter(name__istartswith='a')
    # data=student2.objects.filter(name__endswith='a')
    # data=student2.objects.filter(name__iendswith='n')
    # data=student2.objects.filter(mark=84)
    # data=student2.objects.filter(mark__gt=80)
    # data=student2.objects.filter(mark__gte=78).order_by('name')
    # data=student2.objects.filter(mark__lt=80)
    # data=student2.objects.filter(mark__lte=78).order_by('name')
    # data=student1.objects.filter(passdate='2018-12-23')
    # data=student1.objects.filter(passdate__range=('2018-01-01','2020-12-31'))
    # data=student1.objects.filter(passdate__year='2018')
    # data=student1.objects.filter(passdate__month='03')
    # data=student1.objects.filter(passdate__day='29')


    # detail=student2.objects.filter(admdate__date=date(2019,9,11))
    # detail=student2.objects.filter(admdate__date__gt=date(2019,9,11))
    # detail=student2.objects.filter(admdate__date__gte=date(2019,9,11))
    # detail=student2.objects.filter(admdate__year=2019)
    # detail=student2.objects.filter(admdate__year__gt=2019)
    # detail=student2.objects.filter(admdate__year__gte=2019)
    # detail=student2.objects.filter(admdate__month=3)
    # detail=student2.objects.filter(admdate__month__gt=6)
    # detail=student2.objects.filter(admdate__month__gte=6)
    # detail=student2.objects.filter(admdate__quarter=3)
    # detail=student2.objects.filter(admdate__quarter__gt=2)
    # detail=student2.objects.filter(admdate__quarter__gte=2)
    # detail=student2.objects.filter(admdate__week=30)
    # detail=student2.objects.filter(admdate__week__gt=30)
    # detail=student2.objects.filter(admdate__week__gte=30)
    # detail=student2.objects.filter(admdate__week_day=3)
    # detail=student2.objects.filter(admdate__week_day__gt=3)
    # detail=student2.objects.filter(admdate__week_day__gte=3)

#########for some mathematical operations...................
    data=student1.objects.all()
    total=data.aggregate(Sum('mark'))
    average=data.aggregate(Avg('mark'))
    maximum=data.aggregate(Max('mark'))
    minimum=data.aggregate(Min('mark'))
    nctotal=data.aggregate(Count('mark'))

    totalcount=data.count()
    context={'alldata':data,'alldetail':detail,'count':totalcount,'total':total,'average':average,'maximum':maximum,'minimum':minimum,'nctotal':nctotal}

    return render(request,'queryset.html',context)
