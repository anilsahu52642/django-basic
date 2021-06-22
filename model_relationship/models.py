from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#################################################################
###########for one to one relationship(one object for one user)
class onepage(models.Model):
    ######if user is deleted then page will also delete.....
    creater=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    ######if user is deleted then first we have to delete the page of user
    # creater=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    ########create page if user has staff_status=True
    # creater=models.OneToOneField(User,on_delete=models.CASCADE,limit_choices_to={'staff_status':True})
    pagename=models.CharField(max_length=64)
    pagecatagory=models.CharField(max_length=64)

class likethepage(onepage):
    page=models.OneToOneField(onepage,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    like=models.IntegerField()



###############################################################################
#####for many to one relationship.............(one user can have multiple page)
class manypage(models.Model):
    creater=models.ForeignKey(User,on_delete=models.CASCADE)
    # creater=models.ForeignKey(User,on_delete=models.PROTECT)
    ##############here because of below line program if user is deleted then corrosponding page will not delete it will asign as null
    # creater=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    pagename=models.CharField(max_length=64)

##############################################################################
###############For many to many relationship(one user can have multiple page and one page can be shared by many page)
class song(models.Model):
    singer=models.ManyToManyField(User)
    song_name=models.CharField(max_length=64)
    song_duration=models.IntegerField()

    def written(self):
        return ','.join([str(s) for s in self.singer.all()])
