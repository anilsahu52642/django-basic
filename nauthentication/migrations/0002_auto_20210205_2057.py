# Generated by Django 3.1.4 on 2021-02-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nauthentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='email',
            field=models.EmailField(default='add', max_length=64),
        ),
        migrations.AddField(
            model_name='people',
            name='fname',
            field=models.CharField(default='add', max_length=64),
        ),
        migrations.AddField(
            model_name='people',
            name='lname',
            field=models.CharField(default='add', max_length=64),
        ),
    ]
