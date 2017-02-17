from accounts.models import Customer


def customer_exists(email):
    try:
        customer = Customer.objects.get(customer_email=email)
        if customer is not None:
            return True
        else:
            return False
    except Customer.DoesNotExist:
        return False
