import datetime
from order.models import OrderPayment


def get_order_payment(order_id):
    order_payment = OrderPayment.objects.get(order__id=order_id)
    return order_payment


def get_undelivered_order_payments():
    order_payments = OrderPayment.objects.all().filter(delivered=False, order__complete_status=True)
    return order_payments


def get_delivered_order_payments():
    order_payments = OrderPayment.objects.all().filter(delivered=True)
    return order_payments


def update_order_payment(order, paid_amount, place):
    order_payment = OrderPayment.objects.get(order=order)

    new_balance = order_payment.balance - paid_amount
    storage_days = abs((order_payment.order.order_completion_date - datetime.datetime.now().date()).days)
    new_storage_fee = 5000 * storage_days

    if place == 'Nairobi':
        delivery_fee = 1500
    elif place == 'personal':
        delivery_fee = 0
    else:
        delivery_fee = 4500

    delivery_or_collection_date = datetime.datetime.now().date()
    delivered = True

    order_payment.balance = new_balance
    order_payment.after_completion_days = storage_days
    order_payment.storage_fee = new_storage_fee
    order_payment.delivery_fee = delivery_fee
    order_payment.delivery_or_collection_date = delivery_or_collection_date
    order_payment.delivered = delivered

    order_payment.save()
