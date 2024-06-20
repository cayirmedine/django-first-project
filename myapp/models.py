from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.TextField()
    img_url = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) #You can use null=True instead of default=True, if you want default null value
    category = models.CharField(max_length=50, null=True) #blank means null string

    def __str__(self):
        return f"{self.name} {self.price}"