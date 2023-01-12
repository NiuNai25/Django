from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django import forms
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
import random
from decimal import Decimal


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')    

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
                item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity']
                                                                          ,'update': True})
                                                                 
    for item in cart:
        item['total_price'] = item['price'] *  item['quantity']
        
    products = Product.objects.filter(available=True)
    option = random.sample(range(1, 9), 3)
    return render(request, 'cart/detail.html', {'cart': cart,
    'products': products,'option':option, 
})
