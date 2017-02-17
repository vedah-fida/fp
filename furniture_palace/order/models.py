from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_complete = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    order_completion_date = models.DateField()
    customer = models.ForeignKey('accounts.Customer', null=False, unique=False)
    carpenter = models.ForeignKey(User, null=True, unique=False)
    temp_carpenter = models.ForeignKey('accounts.TempCarpenter', null=True, unique=False)

    def __str__(self):
        return self.order_name
