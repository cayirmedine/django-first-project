from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.TextField()
    img_url = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) #You can use null=True instead of default=True, if you want default null value
    #category = models.CharField(max_length=50, null=True) #blank means null string
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="products")
    slug = models.SlugField(default="", null=False, db_index=True, unique=True, blank=True) 
    # null=False equals to not nullable
    #if you define primary_key=True then automatically defined as unique=True
    #if you use primary_key then id not created automatically
    #blank=True means you dont need to enter slug value in form
    #if you use editable=False, defined attr does not display in admin form 

    def __str__(self):
        return f"{self.name} {self.price} {self.slug}"