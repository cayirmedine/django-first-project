from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active", "slug")
    readonly_fields = ["slug"]
    list_display_links = ("name", "slug")
    list_filter = ("name", "price", "category")
    list_editable = ["is_active"]
    search_fields = ("name", "description")

# Register your models here.
admin.site.register(Product, ProductAdmin) #introduce Product model to admin
