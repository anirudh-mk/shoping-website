from django.db import models


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




