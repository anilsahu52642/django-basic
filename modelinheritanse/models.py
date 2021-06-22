from django.db import models
from .managers import customanil1
# Create your models here.
class chairman(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True
#################for abstact class no model is created for parent class

class teacher(chairman):
##########date field is not required and new salary field is added
    salary=models.IntegerField()
    date=None
    ###########for default manager ................here manager is objects........(objects=models.Manager())
    ###########for our own manager name ................here manager is anil1........)
    # anil1=models.Manager()
    ###########for custom manager ................here manager is anil4........)
    anil4=customanil1()

class student3(chairman):
##########new field is added
    roll=models.IntegerField()
    ###########for default manager ................here manager is objects........(objects=models.Manager())
    ###########for our own manager name ................here manager is anil2........)
    # anil2=models.Manager()
    ###########for custom manager ................here manager is anil5........)
    anil5=customanil1()
class contractor(chairman):
###########date field is overloaded
    date=models.DateTimeField()
    ###########for default manager ................here manager is objects........(objects=models.Manager())
    ###########for our own manager name ................here manager is anil3........)
    # anil3=models.Manager()
    ###########for custom manager ................here manager is anil6........)
    anil6=customanil1()





###########################################################################################
##########for proxy model here two model is created see from admin page but one table is created see in database browser)
##########if one object of any model is created or deleted then corrosponding object from other model is created or deleted

class examcenter(models.Model):
    centername=models.CharField(max_length=64)
    centerloc=models.CharField(max_length=64)

class myexamcenter(examcenter):
    class Meta:
        proxy=True



##########################################################################################################
############for multitable inheritanse...........here for two model two table is alse created
############# here if one object is created or deleted in animal model then corrosponding object is created or deleted in creature model also ....but if we created one object in creature then no object is created in animalbut if we deleted one object then if corrosponding object available in animal model then it will delete....

class creature(models.Model):
    name=models.CharField(max_length=64)

class animal(creature):
    legs=models.IntegerField()
