from django.contrib import admin
from order.models import Order, OrderPayment


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_name',
        'order_date',
        'order_completion_date',
        'complete_status',
        'order_price',
        'customer',
        'carpenter',
    )
    list_display_links = ('order_name',)


admin.site.register(Order, OrderAdmin)


class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'deposit',
        'balance',
        'days_in_store',
        'storage_fee',
        'delivery_fee',
        'delivery_or_collection_date',
        'delivered',
    )


admin.site.register(OrderPayment, OrderPaymentAdmin)
