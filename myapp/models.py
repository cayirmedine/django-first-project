from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.TextField()
    img_url = models.CharField(max_length=50)