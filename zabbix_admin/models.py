from django.db import models

# Create your models here.

class Agent(models.Model):
    host = models.CharField(max_length=255)
