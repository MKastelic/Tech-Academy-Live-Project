# Generated by Django 2.1.5 on 2019-02-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataApp', '0007_merge_20190206_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseballTeam',
            fields=[
                ('team_id', models.CharField(max_length=50)),
                ('team_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]