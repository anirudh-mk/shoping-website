from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=400, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100)



