from django.contrib import admin
from catalog.models import *


# Register your models here.
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('furniture_name', 'furniture_category',)


admin.site.register(Furniture, FurnitureAdmin)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'lending_rate_per_day',)


admin.site.register(Tool, ToolAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'per_unit_price',)


admin.site.register(Material, MaterialAdmin)
