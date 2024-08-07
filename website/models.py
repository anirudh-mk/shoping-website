from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    CHOICES = [
        ('mens', 'mens'),
        ('womens', 'womens'),
        ('kids', 'kids'),
        ('sports', 'sports'),
        ('reguler', 'reguler')
    ]
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    is_new = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    catogery = models.CharField(max_length=200, choices=CHOICES)

    def __str__(self):
        return self.name


class UserCart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)


class Order(models.Model):
    CHOICES = [
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200, choices=CHOICES)





