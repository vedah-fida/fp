import datetime
from order.models import Order, OrderPayment
from accounts.models import Customer
from django.contrib.auth.models import User
from accounts.models import TempCarpenter


# create new order and associate it with order payment
def save_order(customer_id, order_name, quantity, order_price, deposit):
    new_order = Order()

    new_order.customer = Customer.objects.get(id=customer_id)
    new_order.order_name = order_name
    new_order.quantity = quantity
    new_order.order_price = order_price
    new_order.save()

    # creating its order payment associate
    new_order_payment = OrderPayment()

    new_order_payment.order = new_order
    new_order_payment.deposit = deposit
    new_order_payment.balance = (order_price - deposit)
    new_order_payment.payment_percentage = (deposit / order_price) * 100
    new_order_payment.save()


def get_order(order_id):
    order = Order.objects.get(id=order_id)
    return order


def change_order_status(order_id, status):
    # get order to change
    order = Order.objects.get(id=order_id)

    # change status of order
    order.complete_status = status
    # register date of completion
    order.order_completion_date = datetime.datetime.now().date()
    # save change
    order.save()


# get all order made by a certain customer
def get_orders_for(customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders_for_customer = Order.objects.filter(customer=customer).order_by('-order_date')
    # return orders for specific customer
    return orders_for_customer


def get_complete_orders():
    orders = Order.objects.filter(complete_status=True).order_by('-order_date')
    return orders


def get_incomplete_orders():
    orders = Order.objects.filter(complete_status=False).order_by('-order_date')
    return orders


# get all orders ever made sorted by the date which the order was made
def get_all_orders():
    orders = Order.objects.all().order_by('-order_date')
    # return all orders
    return orders


def search_for_orders(query, field):
    if field == 'customer':
        orders = Order.objects.filter(customer__customer_name__icontains=query)
        return orders
    elif field == 'carpenter':
        orders = Order.objects.filter(carpenter__username__icontains=query)
        return orders
    elif field == 'order_name':
        orders = Order.objects.filter(order_name__icontains=query)
        return orders
    elif field == 'temp_carpenter':
        orders = Order.objects.filter(temp_carpenter__temp_carpenter_name__icontains=query)
        return orders
    else:
        orders = Order.objects.all()
        return orders


def get_unassigned_orders():
    orders = Order.objects.filter(carpenter=None, temp_carpenter=None).order_by('-order_date')
    return orders


def get_carpenter_orders(carpenter_id):
    carpenter = User.objects.get(id=carpenter_id)
    carpenter_orders = Order.objects.filter(carpenter=carpenter)
    return carpenter_orders


# assign an order to the carpenter
def assign_order_self(user, order_id):
    order = Order.objects.get(id=order_id)
    order.carpenter = user
    order.save()


def assign_order_to(temp_carpenter_id, carpenter, order_id):
    # get the order to be assigned and the temporary carpenter
    order = Order.objects.get(id=order_id)
    temp_carpenter = TempCarpenter.objects.get(id=temp_carpenter_id)
    # assign the order to the carpenter("supervisor") and the temporary carpenter
    order.carpenter = carpenter
    order.temp_carpenter = temp_carpenter
    # save the order
    order.save()


# delete order
def remove_order(order_id):
    # get order to delete from the database
    order_to_remove = Order.objects.get(id=order_id)
    # delete the order fetched
    order_to_remove.delete()


def carpenter_active_orders(carpenter):
    active_orders = Order.objects.filter(carpenter=carpenter, complete_status=False,
                                         temp_carpenter=None).count()

    if active_orders:
        return active_orders
    else:
        active_orders = 0
        return active_orders
