from django.db import models

# Create your models here.
class student1(models.Model):
    name=models.CharField(max_length=64)
    roll=models.IntegerField()
    city=models.CharField(max_length=64)
    mark=models.IntegerField()
    passdate=models.DateField()


class student2(models.Model):
    name=models.CharField(max_length=64)
    roll=models.IntegerField()
    city=models.CharField(max_length=64)
    mark=models.IntegerField()
    passdate=models.DateField()
    admdate=models.DateTimeField()
