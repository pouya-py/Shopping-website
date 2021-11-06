from django.shortcuts import render,redirect,get_object_or_404
from orders.models import Order
import braintree
from django.conf import settings
from .task import payment_completed
#instantiate braintree gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce',None)
        # create and submit transactions
        result =gateway.transaction.sale({
            'amount':f'{total_cost:.2f}',
            'payment_method_nonce':nonce,
            'options':{
                'submit_for_settlement':True
            }
        })
        if result.is_success:
            # if result was successful,mark paid to True.
            order.paid = True
            # also store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            # asynchronous task
            payment_completed.delay(order.id)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    # generate token
    else:
        client_token = gateway.client_token.generate()
        return render(request, 'payment/process.html',{
            'client_token': client_token,
            'order': order,
        })

def payment_done(request):
    return render(request,'payment/done.html')

def payment_canceled(request):
    return render(request,'payment/canceled.html')


    
