from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.filters import ListFilter
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = [
        'code','valid_from','valid_to',
        'discount','active'
    ]
    list_filter = ['active','valid_from','valid_to',]
    search_fiels = ['code']
    