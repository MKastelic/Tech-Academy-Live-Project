from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zip_code = models.IntegerField()
    favorite_hockey_team = models.CharField(max_length=50, default='')

class HockeyTeam(models.Model):
    team_id = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50, primary_key=True)
