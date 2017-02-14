from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_class', 'customer_tel_no',)


admin.site.register(Customer, CustomerAdmin)


class CarpenterAdmin(admin.ModelAdmin):
    list_display = ('carpenter_name', 'carpenter_email',)


admin.site.register(Carpenter, CarpenterAdmin)


class TempCarpenterAdmin(admin.ModelAdmin):
    list_display = ('temp_carpenter_name', 'carpenter',)


admin.site.register(TempCarpenter, TempCarpenterAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'order_complete',)


admin.site.register(Order, OrderAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'material_price',)


admin.site.register(Material, MaterialAdmin)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool_name',)


admin.site.register(Tool, ToolAdmin)


class BedAdmin(admin.ModelAdmin):
    list_display = ('category', 'bed_price',)


admin.site.register(Bed, BedAdmin)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('category', 'seat_price',)


admin.site.register(Seat, SeatAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ('category', 'table_price',)


admin.site.register(Table, TableAdmin)
