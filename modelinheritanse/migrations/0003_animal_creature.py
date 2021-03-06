# Generated by Django 3.1.4 on 2021-02-27 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritanse', '0002_auto_20210227_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='animal',
            fields=[
                ('creature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelinheritanse.creature')),
                ('legs', models.IntegerField()),
            ],
            bases=('modelinheritanse.creature',),
        ),
    ]
