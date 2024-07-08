from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.TextField()
    img_url = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) #You can use null=True instead of default=True, if you want default null value
    category = models.CharField(max_length=50, null=True) #blank means null string
    slug = models.SlugField(default="", null=False) # null=False equals to not nullable

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.name} {self.price}"