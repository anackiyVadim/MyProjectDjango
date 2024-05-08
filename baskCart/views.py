from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .baskCart import Cart
from .forms import CartAddProductForm
from firstApp.models import Product
from firstApp.views import base


# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('baskCart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('baskCart:cart_detail')

def cart_detail(request):
    baskCart = Cart(request)
    context = {'baskCart': baskCart}
    context.update(base())
    return render(request, 'baskCart/detail.html', context)
