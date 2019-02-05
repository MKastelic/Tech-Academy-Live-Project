from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50, default='Portland')
    state = models.CharField(max_length=50, default='OR')