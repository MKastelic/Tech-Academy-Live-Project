from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    recipient = models.CharField(max_length=50)
    date_sent = models.DateTimeField()
    message_body = models.TextField()
