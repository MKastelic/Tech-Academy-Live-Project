# Generated by Django 2.1.5 on 2019-02-07 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataApp', '0008_baseballteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite_mlb_team',
            field=models.CharField(default='', max_length=50),
        ),
    ]
