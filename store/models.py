from django.db import models
from cartegory.models import Cartegory
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug= models.SlugField(max_length=255, unique=True)
    product_description = models.TextField(max_length=555, blank=True)
    price= models.IntegerField()
    images=models.ImageField(upload_to='photos/product', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    cartegory= models.ForeignKey(Cartegory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.cartegory.slug, self.slug])
    
    def __str__(self):
        return self.product_name
    
    
    