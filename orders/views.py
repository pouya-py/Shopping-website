from django.shortcuts import render,redirect
from .tasks import order_created
from .models import OrderItem
from cart.cart import Cart 
from .forms import OrderCreateForm

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order= order,
                    product = item['product'],
                    price = item['price'],
                    quantity = item['quantity']
                )
            cart.clear()
            # launch  asynchronous task
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
            {'order':order}
            )
    form = OrderCreateForm()
    return render(request,'orders/order/create.html', 
    {'form':form, 'cart':cart})