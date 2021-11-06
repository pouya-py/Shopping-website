from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order
import weasyprint

@shared_task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)

    # Invoice email
    subject = f'My shop - EE invoice no. {order.id}'
    message = 'You can see the attached recent purchase in the attachment files.'
    email = EmailMessage(
        subject,
        message,
        'admin@gmail.com',
        [order.email]
    )
    # generate pdf
    html = render_to_string('orders/order/pdf.html',{'order':order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)

    # attach pdf file
    email.attach(f'order_{order.id}.pdf',out.getvalue(),'application/pdf')
    email.send()