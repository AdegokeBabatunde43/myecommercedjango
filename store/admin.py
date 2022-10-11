from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'modify_date', 'created_date', 'stock', 'price')
    list_display_links=('product_name', 'modify_date', 'created_date', 'stock', 'price')
    prepopulated_fields={'slug': ['product_name'],}
    

admin.site.register(Product, ProductAdmin)