from django.shortcuts import render
# Create your views here.
from .models import OrderItem, OrderItemUser
from .forms import OrderCreateForm, OrderUserCreateForm
from baskCart.baskCart import Cart
from firstApp.views import base
import asyncio


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        # print(form.errors)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            asyncio.run(form.send_message())
            context = {'order': order}
            context.update(base())
            return render(request, 'orders/created.html', context)
    else:
        form = OrderCreateForm
    context = {'cart': cart, 'form': form}
    context.update(base())
    return render(request, 'orders/create.html', context)

def order_create_user(request):
    cart = Cart(request)
    if request.method == 'POST':
        formUser = OrderUserCreateForm(request.POST, user=request.user)
        print(formUser.errors)
        if formUser.is_valid():
            order = formUser.save()
            for item in cart:
                OrderItemUser.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            # asyncio.run(formUser.send_message_user())
            context = {'order': order}
            context.update(base())
            return render(request, 'orders/created.html', context)
    else:
        formUser = OrderUserCreateForm
    context = {'cart': cart, 'formUser':formUser}
    context.update(base())
    return render(request, 'orders/create_user.html', context)
