# Generated by Django 3.1.4 on 2021-02-27 16:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritanse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='examcenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centername', models.CharField(max_length=64)),
                ('centerloc', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterModelManagers(
            name='contractor',
            managers=[
                ('anil6', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='student3',
            managers=[
                ('anil5', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
                ('anil4', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='myexamcenter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('modelinheritanse.examcenter',),
        ),
    ]
