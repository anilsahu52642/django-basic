from django.db import models

# Create your models here.

class image(models.Model):
    ########### here because of below line code uploaded images are keep inside 'images' folder.....but to finding path we have to write some code inside settings.py file to give path when we click to see uploaded image inside admin page
    ########### in below program because of auto_now_add=True    it saves current date and time when uploading ..........so date field will not shown in database
    photo=models.ImageField(upload_to='images')
    date=models.DateTimeField(auto_now_add=True)



########## after writing code in models.py and admin.py file we have to install library pillow ....
##### in cmd type     pip install pillow


########## after uploading image in database if in the database we click on image then it will show error because it cant find the path so we have to write some code inside urls.py file......
