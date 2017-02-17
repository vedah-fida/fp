from django.forms import ModelForm
from accounts.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'customer_tel_no', 'customer_address', 'customer_class']
