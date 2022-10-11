from django.shortcuts import render, get_object_or_404
from cartegory.models import Cartegory
from .models import Product

# Create your views here.
def store(request, cartegory_slug=None):
    cartegories=None
    products= None
    
    if cartegory_slug != None:
        cartegories=get_object_or_404(Cartegory, slug=cartegory_slug)
        products=Product.objects.filter(cartegory=cartegories, is_available=True)
        product_count=products.count()
    else:
        
        products=Product.objects.all().filter(is_available=True)
        product_count=products.count()
    context= {'products': products, 'product_count':product_count}
    return render(request, 'store/store.html', context)





def product_detail(request, cartegory_slug, product_slug):
    try:
        single_product = Product.objects.get(cartegory__slug=cartegory_slug, slug=product_slug)
    except Exception as e:
        raise e
    context={'single_product':single_product,}     
    return render(request, 'store/product_detail.html', context)

