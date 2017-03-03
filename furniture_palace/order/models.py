from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    order_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    complete_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    order_price = models.FloatField(null=True)
    order_completion_date = models.DateField(null=True)
    customer = models.ForeignKey('accounts.Customer', null=False, unique=False)
    carpenter = models.ForeignKey(User, null=True, unique=False)
    temp_carpenter = models.ForeignKey('accounts.TempCarpenter', null=True, unique=False)

    def __str__(self):
        return "Order Id " + str(self.id) + " | " + self.order_name


class OrderPayment(models.Model):
    order = models.OneToOneField(Order,
                                 on_delete=models.CASCADE,
                                 primary_key=True)

    deposit = models.FloatField()
    balance = models.FloatField()
    days_in_store = models.IntegerField(default=0)
    storage_fee = models.FloatField(default=0.00)
    delivery_fee = models.FloatField(default=0.00)
    delivery_or_collection_date = models.DateField(null=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order.id) + ", " + self.order.order_name
