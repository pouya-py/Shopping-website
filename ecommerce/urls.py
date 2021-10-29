
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',include('cart.urls',namespace='cart')),
    path('payment/',include('payment.urls',namespace='payment')),
    path('orders/',include('orders.urls',namespace='orders')),
    path('',include('shop.urls',namespace='shop')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    