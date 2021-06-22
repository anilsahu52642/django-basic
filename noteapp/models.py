from django.db import models

# Create your models here.

class imageupload2(models.Model):
    photo=models.ImageField(upload_to='notes')
    date=models.DateTimeField(auto_now_add=True)
