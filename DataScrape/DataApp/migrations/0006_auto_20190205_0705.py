# Generated by Django 2.1.5 on 2019-02-05 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataApp', '0005_auto_20190204_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favorite_hockey_team',
            new_name='favorite_nhl_team',
        ),
    ]
