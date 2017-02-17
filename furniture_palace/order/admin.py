from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_name',
        'order_date',
        'order_completion_date',
        'order_complete',
        'order_price',
        'customer',
        'carpenter',
    )


admin.site.register(Order, OrderAdmin)
