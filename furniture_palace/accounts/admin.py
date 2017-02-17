from django.contrib import admin
from accounts.models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_class', 'customer_tel_no',)


admin.site.register(Customer, CustomerAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('carpenter', 'carpenter_tel_no', 'carpenter_salary', 'commission',)


admin.site.register(Profile, ProfileAdmin)


class TempCarpenterAdmin(admin.ModelAdmin):
    list_display = ('temp_carpenter_name', 'temp_carpenter_email',)


admin.site.register(TempCarpenter, TempCarpenterAdmin)
