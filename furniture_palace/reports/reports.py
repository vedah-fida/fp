from order.models import Order, OrderPayment
from accounts.models import User, Profile
from reports.models import LentTool


def get_all_orders():
    complete_orders = Order.objects.filter(complete_status=True)
    return complete_orders


def get_carpenter_orders(user):
    carpenter_orders = Order.objects.filter(carpenter=user, temp_carpenter=None)
    return carpenter_orders


def get_carpenter_order_totals_commission(user):
    profile = Profile.objects.get(carpenter=user)
    carpenter_order_totals = 0
    orders = get_carpenter_orders(user)
    for order in orders:
        carpenter_order_totals += (order.order_price * float(profile.commission / 100))
    return carpenter_order_totals


def get_assigned_orders(user):
    assigned_orders = Order.objects.filter(carpenter=user).exclude(temp_carpenter=None)
    return assigned_orders


def get_assigned_order_totals_commission(user):
    assigned_order_total = 0
    orders = get_assigned_orders(user)
    for order in orders:
        assigned_order_total += (float(order.order_price) * 0.01)
    return assigned_order_total


def get_salary(user):
    profile = Profile.objects.get(carpenter=user)
    salary = profile.carpenter_salary

    return salary

def total_commission(user):
    return float(get_assigned_order_totals_commission(user)) + float(get_carpenter_order_totals_commission(user))


def carpenter_gross_salary(user):
    return float(get_salary(user)) + total_commission(user)


def get_orders_totals():
    order_totals = 0
    orders = get_all_orders()
    for order in orders:
        order_totals += order.order_price
    return order_totals


def get_carpenters():
    carpenters = User.objects.exclude(username="wolf")
    return carpenters


def get_salary_totals():
    salary_totals = 0
    carpenter_profile = Profile.objects.all()
    for profile in carpenter_profile:
        salary_totals += profile.carpenter_salary
    return salary_totals


def get_carpenter_commissions_subtotals():
    commission_percentage = 2
    supervised_order_commission_percentage = 1

    supervised_commission_totals, carpenter_commission_totals = 0, 0
    carpenter_orders = Order.objects.filter(complete_status=True, temp_carpenter=None)
    supervised_orders = Order.objects.filter(completer_status=True).exclude(temp_carpenter=None)
    for carpenter_order in carpenter_orders:
        carpenter_commission_totals += (carpenter_order.order_price * (commission_percentage / 100))

    for supervised_order in supervised_orders:
        supervised_commission_totals += (supervised_order.order_price * (supervised_order_commission_percentage / 100))

    return carpenter_commission_totals + supervised_commission_totals


def get_temp_carpenter_commissions_subtotals():
    temp_carpenter_commission_totals = 0
    temp_carpenter_commission_percentage = 3
    assigned_orders = Order.objects.filter(completer_status=True).exclude(temp_carpenter=None)
    for order in assigned_orders:
        temp_carpenter_commission_totals += (order.order_price * (temp_carpenter_commission_percentage / 100))
    return temp_carpenter_commission_totals


def get_commissions_grand_totals():
    return get_carpenter_commissions_subtotals() + get_temp_carpenter_commissions_subtotals()


def get_tool_damage_fees():
    damage_fee_totals = 0
    lent_tools = LentTool.objects.all()
    for lent_tool in lent_tools:
        damage_fee_totals += lent_tool.damage_fee
    return damage_fee_totals


def get_storage_fees():
    storage_fee_totals = 0
    order_payments = OrderPayment.objects.all()
    for order_payment in order_payments:
        storage_fee_totals += order_payment.storage_fee
    return storage_fee_totals
