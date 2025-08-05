from django.db import models

# Create your models here.

class Project(models.Model):
    thumbnail = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    customer = models.CharField(max_length=75)
    category = models.CharField(max_length=75)
    date = models.CharField(max_length=75)
    tech = models.CharField(max_length=120)
    project_url = models.CharField(max_length=150)
    picture1 = models.CharField(max_length=250)
    picture2 = models.CharField(max_length=250)
    picture3 = models.CharField(max_length=250)
    picture4 = models.CharField(max_length=250)
