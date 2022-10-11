
from django.db import models
from django.urls import reverse

# Create your models here.
class Cartegory(models.Model):
    cartegory_name= models.CharField(max_length=50)
    slug= models.SlugField(max_length=100, unique=True)
    description= models.TextField(max_length=255, blank=True)
    cart_image= models.ImageField(upload_to='photos/cartgories', blank=True)
    
    
    class Meta:
        verbose_name='Cartegory'
        verbose_name_plural='Cartegories'
        
    def get_url(self):
        return reverse('products_by_cartegory', args=[self.slug])
    
    def __str__(self):
        return self.cartegory_name
    
    
