from django.contrib import admin
from catalog.models import *


# Register your models here.
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('furniture_name', 'furniture_category', 'material_price')


admin.site.register(Furniture, FurnitureAdmin)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'lending_rate_per_day',)


admin.site.register(Tool, ToolAdmin)


class LentToolAdmin(admin.ModelAdmin):
    list_display = (
        'tool',
        'temp_carpenter',
        'lend_date',
        'return_date',
        'lending_fee',
    )


admin.site.register(LentTool, LentToolAdmin)
