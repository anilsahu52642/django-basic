from faker import Faker
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','basic_project1.settings')
django.setup()
from random import *
from nauthentication.models import people


fake=Faker()
def populate(n):
    for i in range(n):
        n=fake.name()
        fn=fake.first_name()
        ln=fake.random_element(elements=('sahu','senapati','nayak','jena'))
        e=fake.email()
        x=people.objects.get_or_create(name=n,fname=fn,lname=ln,email=e)


populate(10)



################### create the file inside folder where manage.py file available...
########## after this to generate fake data type (py populate.py) inside terminal and runserver to see added data in database


########## after this inside terminal type (py populate.py)
