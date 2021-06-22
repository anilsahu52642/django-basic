from django.db import models

# Create your models here.
class people(models.Model):
    name=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    password2=models.CharField(max_length=64)
    email=models.EmailField(max_length=64,default='add')
    fname=models.CharField(max_length=64,default='add')
    lname=models.CharField(max_length=64,default='add')
