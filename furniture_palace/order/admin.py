from django.contrib import admin
from order.models import Order, OrderPayment


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_name',
        'order_date',
        'order_completion_date',
        'complete_status',
        'order_price',
        'customer',
        'carpenter',
    )


admin.site.register(Order, OrderAdmin)


class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'deposit',
        'balance',
        'storage_fee',
    )


admin.site.register(OrderPayment, OrderPaymentAdmin)
