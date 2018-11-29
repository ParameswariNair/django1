from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=50)
    location =models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class project1(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role= models.CharField(max_length=50,default="admin")