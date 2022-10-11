from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:cartegory_slug>/', views.store, name='products_by_cartegory'),
    path('<slug:cartegory_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]