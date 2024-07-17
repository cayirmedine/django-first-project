from django.contrib import admin
from .models import Product, Category, Address, Supplier

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active", "slug", "selected_categories")
    #readonly_fields = ["slug"]
    prepopulated_fields = { "slug": ["name"] }
    list_display_links = ("name", "slug")
    list_filter = ("name", "price", "categories")
    list_editable = ["is_active"]
    search_fields = ("name", "description")

    def selected_categories(self, obj):
        html = ""

        categories = obj.categories.all()

        for cat in categories:
            html += cat.name + " "

        return html

# Register your models here.
admin.site.register(Product, ProductAdmin) #introduce Product model to admin
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Supplier)
