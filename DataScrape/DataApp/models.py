from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50, default='Portland')
    state = models.CharField(max_length=50, default='OR')
    favorite_nhl_team = models.CharField(max_length=50, default='')
    favorite_mlb_team = models.CharField(max_length=50, default='')

class HockeyTeam(models.Model):
    team_id = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50, primary_key=True)

class BaseballTeam(models.Model):
    team_id = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50, primary_key=True)
