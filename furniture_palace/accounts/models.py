from django.db import models
from django.contrib.auth.models import User


# models
class Profile(models.Model):
    carpenter_tel_no = models.CharField(max_length=100)
    carpenter_address = models.CharField(max_length=100)
    carpenter_salary = models.DecimalField(max_digits=9, decimal_places=2)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    carpenter = models.OneToOneField(User,
                                     on_delete=models.CASCADE,
                                     primary_key=True, )

    def __str__(self):
        return self.carpenter.username


class TempCarpenter(models.Model):
    temp_carpenter_name = models.CharField(max_length=100)
    temp_carpenter_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.temp_carpenter_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=254, unique=True)
    customer_tel_no = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=255)
    customer_physical_address = models.TextField()
    # customer type according to order made
    gold, silver = 'Gold', 'Silver'
    customer_type_choices = (
        (gold, 'GOLD'),
        (silver, 'SILVER'),
    )
    customer_class = models.CharField(
        max_length=15,
        choices=customer_type_choices,
        default=silver,
    )

    def __str__(self):
        return self.customer_name
