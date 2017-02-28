from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    order_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    complete_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    order_completion_date = models.DateField(null=True)
    customer = models.ForeignKey('accounts.Customer', null=False, unique=False)
    carpenter = models.ForeignKey(User, null=True, unique=False)
    temp_carpenter = models.ForeignKey('accounts.TempCarpenter', null=True, unique=False)

    def __str__(self):
        return str(self.id) + ", " + self.order_name


class OrderPayment(models.Model):
    order = models.OneToOneField(Order,
                                 on_delete=models.CASCADE,
                                 primary_key=True)

    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    storage_fee = models.FloatField(default=0)

    def __str__(self):
        return str(self.order.id) + ", " + self.order.order_name
