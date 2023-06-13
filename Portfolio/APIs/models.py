
# Create your models here.
from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    projects = models.TextField()