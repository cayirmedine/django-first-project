from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active", "slug", "category")
    #readonly_fields = ["slug"]
    prepopulated_fields = { "slug": ["name"] }
    list_display_links = ("name", "slug")
    list_filter = ("name", "price", "category")
    list_editable = ["is_active"]
    search_fields = ("name", "description")

# Register your models here.
admin.site.register(Product, ProductAdmin) #introduce Product model to admin
admin.site.register(Category)
