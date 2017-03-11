from datetime import datetime
from order.models import Order, OrderPayment
from accounts.models import Profile
from catalog.models import LentTool


def current_month():
    year = datetime.now().year
    month = datetime.now().month
    return {'year': year, 'month': month}


def previous_month():
    if datetime.now().month == 1:
        pre_month = 12
        year = datetime.now().year - 1
    else:
        pre_month = datetime.now().month - 1
        year = datetime.now().year
    return {'year': year, 'pre_month': pre_month}


def get_all_complete_orders_current():
    year = current_month()['year']
    month = current_month()['month']
    complete_orders = Order.objects.filter(complete_status=True, order_date__month=month, order_date__year=year)
    return complete_orders


def get_all_complete_orders_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    complete_orders = Order.objects.filter(complete_status=True, order_date__month=month, order_date__year=year)
    return complete_orders


def get_carpenter_orders_current(user):
    year = current_month()['year']
    month = current_month()['month']
    carpenter_orders = Order.objects.filter(carpenter=user, temp_carpenter=None, order_date__month=month,
                                            order_date__year=year)
    return carpenter_orders


def get_carpenter_orders_previous(user):
    year = previous_month()['year']
    month = previous_month()['pre_month']
    carpenter_orders = Order.objects.filter(carpenter=user, temp_carpenter=None, order_date__month=month,
                                            order_date__year=year)
    return carpenter_orders


def get_carpenter_order_totals_commission_current(user):
    profile = Profile.objects.get(carpenter=user)
    carpenter_order_totals = 0
    orders = get_carpenter_orders_current(user)
    for order in orders:
        carpenter_order_totals += (order.order_price * float(profile.commission / 100))
    return carpenter_order_totals


def get_carpenter_order_totals_commission_previous(user):
    profile = Profile.objects.get(carpenter=user)
    carpenter_order_totals = 0
    orders = get_carpenter_orders_previous(user)
    for order in orders:
        carpenter_order_totals += (order.order_price * float(profile.commission / 100))
    return carpenter_order_totals


def get_assigned_orders_current(user):
    year = current_month()['year']
    month = current_month()['month']
    assigned_orders = Order.objects.filter(carpenter=user, order_date__month=month, order_date__year=year).exclude(
        temp_carpenter=None)
    return assigned_orders


def get_assigned_orders_previous(user):
    year = previous_month()['year']
    month = previous_month()['pre_month']
    assigned_orders = Order.objects.filter(carpenter=user, order_date__month=month, order_date__year=year).exclude(
        temp_carpenter=None)
    return assigned_orders


def get_assigned_order_totals_commission_current(user):
    assigned_order_total = 0
    orders = get_assigned_orders_current(user)
    for order in orders:
        assigned_order_total += (float(order.order_price) * 0.01)
    return assigned_order_total


def get_assigned_order_totals_commission_previous(user):
    assigned_order_total = 0
    orders = get_assigned_orders_previous(user)
    for order in orders:
        assigned_order_total += (float(order.order_price) * 0.01)
    return assigned_order_total


def get_salary(user):
    profile = Profile.objects.get(carpenter=user)
    salary = profile.carpenter_salary

    return salary


def total_commission_current(user):
    return float(get_assigned_order_totals_commission_current(user)) + float(
        get_carpenter_order_totals_commission_current(user))


def total_commission_previous(user):
    return float(get_assigned_order_totals_commission_previous(user)) + float(
        get_carpenter_order_totals_commission_previous(user))


def carpenter_gross_salary_current(user):
    return float(get_salary(user)) + total_commission_current(user)


def carpenter_gross_salary_previous(user):
    return float(get_salary(user)) + total_commission_previous(user)


def get_orders_totals_current():
    order_totals = 0
    orders = get_all_complete_orders_current()
    for order in orders:
        order_totals += order.order_price
    return order_totals


def get_orders_totals_previous():
    order_totals = 0
    orders = get_all_complete_orders_previous()
    for order in orders:
        order_totals += order.order_price
    return order_totals


def get_carpenter_profiles():
    carpenter_profiles = Profile.objects.all()
    return carpenter_profiles


def get_salary_totals():
    salary_totals = 0
    carpenter_profile = Profile.objects.all()
    for profile in carpenter_profile:
        salary_totals += profile.carpenter_salary
    return salary_totals


def get_carpenter_commissions_subtotals_current():
    commission_percentage = 2
    supervised_order_commission_percentage = 1
    year = current_month()['year']
    month = current_month()['month']

    supervised_commission_totals, carpenter_commission_totals = 0, 0
    carpenter_orders = Order.objects.filter(complete_status=True, temp_carpenter=None, order_date__month=month,
                                            order_date__year=year)
    supervised_orders = Order.objects.filter(complete_status=True, order_date__month=month,
                                             order_date__year=year).exclude(temp_carpenter=None)
    for carpenter_order in carpenter_orders:
        carpenter_commission_totals += (carpenter_order.order_price * (commission_percentage / 100))

    for supervised_order in supervised_orders:
        supervised_commission_totals += (supervised_order.order_price * (supervised_order_commission_percentage / 100))

    return carpenter_commission_totals + supervised_commission_totals


def get_carpenter_commissions_subtotals_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    commission_percentage = 2
    supervised_order_commission_percentage = 1

    supervised_commission_totals, carpenter_commission_totals = 0, 0
    carpenter_orders = Order.objects.filter(complete_status=True, temp_carpenter=None, order_date__month=month,
                                            order_date__year=year)
    supervised_orders = Order.objects.filter(complete_status=True, order_date__month=month,
                                             order_date__year=year).exclude(temp_carpenter=None)
    for carpenter_order in carpenter_orders:
        carpenter_commission_totals += (carpenter_order.order_price * (commission_percentage / 100))

    for supervised_order in supervised_orders:
        supervised_commission_totals += (supervised_order.order_price * (supervised_order_commission_percentage / 100))

    return carpenter_commission_totals + supervised_commission_totals


def get_temp_carpenter_commissions_subtotals_current():
    year = current_month()['year']
    month = current_month()['month']
    temp_carpenter_commission_totals = 0
    temp_carpenter_commission_percentage = 3

    assigned_orders = Order.objects.filter(complete_status=True, order_date__month=month,
                                           order_date__year=year).exclude(temp_carpenter=None)
    for order in assigned_orders:
        temp_carpenter_commission_totals += (order.order_price * (temp_carpenter_commission_percentage / 100))
    return temp_carpenter_commission_totals


def get_temp_carpenter_commissions_subtotals_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    temp_carpenter_commission_totals = 0
    temp_carpenter_commission_percentage = 3
    assigned_orders = Order.objects.filter(complete_status=True, order_date__month=month,
                                           order_date__year=year).exclude(temp_carpenter=None)
    for order in assigned_orders:
        temp_carpenter_commission_totals += (order.order_price * (temp_carpenter_commission_percentage / 100))
    return temp_carpenter_commission_totals


def get_commissions_grand_totals_current():
    return get_carpenter_commissions_subtotals_current() + get_temp_carpenter_commissions_subtotals_current()


def get_commissions_grand_totals_previous():
    return get_carpenter_commissions_subtotals_previous() + get_temp_carpenter_commissions_subtotals_previous()


def get_total_tool_damage_fees_current():
    year = current_month()['year']
    month = current_month()['month']
    damage_fee_totals = 0
    lent_tools = LentTool.objects.all().filter(was_damaged=True, lend_date__month=month, lend_date__year=year)
    for lent_tool in lent_tools:
        damage_fee_totals += lent_tool.tool.damage_fee
    return damage_fee_totals


def get_total_tool_damage_fees_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    damage_fee_totals = 0
    lent_tools = LentTool.objects.all().filter(was_damaged=True, lend_date__month=month, lend_date__year=year)
    for lent_tool in lent_tools:
        damage_fee_totals += lent_tool.tool.damage_fee
    return damage_fee_totals


def get_total_storage_fees_current():
    year = current_month()['year']
    month = current_month()['month']
    storage_fee_totals = 0
    order_payments = OrderPayment.objects.filter(order__order_date__month=month, order__order_date__year=year).exclude(
        days_in_store=0)
    for order_payment in order_payments:
        storage_fee_totals += order_payment.storage_fee
    return storage_fee_totals


def get_total_storage_fees_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    storage_fee_totals = 0
    order_payments = OrderPayment.objects.filter(order__order_date__month=month, order__order_date__year=year).exclude(
        days_in_store=0)
    for order_payment in order_payments:
        storage_fee_totals += order_payment.storage_fee
    return storage_fee_totals


def get_total_lending_fees_current():
    year = current_month()['year']
    month = current_month()['month']
    lending_total_fee = 0
    lent_tools = LentTool.objects.filter(returned=True, lend_date__month=month, lend_date__year=year)
    for lent_tool in lent_tools:
        lending_total_fee += lent_tool.lending_fee
    return lending_total_fee


def get_total_lending_fees_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    lending_total_fee = 0
    lent_tools = LentTool.objects.all().filter(returned=True, lend_date__month=month, lend_date__year=year)
    for lent_tool in lent_tools:
        lending_total_fee += lent_tool.lending_fee
    return lending_total_fee


def get_damaged_tools_current():
    year = current_month()['year']
    month = current_month()['month']
    damaged_tools = LentTool.objects.filter(was_damaged=True, lend_date__month=month, lend_date__year=year)
    return damaged_tools


def get_damaged_tools_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    damaged_tools = LentTool.objects.filter(was_damaged=True, lend_date__month=month, lend_date__year=year)
    return damaged_tools


def get_orders_with_storage_fee_current():
    year = current_month()['year']
    month = current_month()['month']
    orders = OrderPayment.objects.filter(order__order_date__month=month, order__order_date__year=year).exclude(
        days_in_store=0)
    return orders


def get_orders_with_storage_fee_previous():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    orders = OrderPayment.objects.filter(order__order_date__month=month, order__order_date__year=year).exclude(
        days_in_store=0)
    return orders


def get_current_returned_tools():
    year = current_month()['year']
    month = current_month()['month']
    lent_tools = LentTool.objects.filter(lend_date__month=month, lend_date__year=year)
    return lent_tools


def get_previous_returned_tools():
    year = previous_month()['year']
    month = previous_month()['pre_month']
    lent_tools = LentTool.objects.filter(lend_date__month=month, lend_date__year=year)
    return lent_tools
