# Generated by Django 2.1.5 on 2019-01-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataApp', '0003_auto_20190124_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='Portland', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default='Oregon', max_length=50),
        ),
    ]
