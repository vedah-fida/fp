import calendar
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from reports import reports


@login_required(login_url='/')
def show_carpenter_summary(request):
    # current carpenter summary
    carpenter_orders = reports.get_carpenter_orders_current(request.user)
    carpenter_orders_commission_total = reports.get_carpenter_order_totals_commission_current(request.user)
    assigned_orders = reports.get_assigned_orders_current(request.user)
    assigned_orders_commission_total = reports.get_assigned_order_totals_commission_current(request.user)
    total_commission = reports.total_commission_current(request.user)
    salary = reports.get_salary(request.user)
    gross_salary = reports.carpenter_gross_salary_current(request.user)
    orders_commission = float(0.02)
    assigned_order_commission = float(0.01)

    # previous carpenter summary
    previous_carpenter_orders = reports.get_carpenter_orders_previous(request.user)
    previous_carpenter_orders_commission_total = reports.get_carpenter_order_totals_commission_previous(request.user)
    previous_assigned_orders = reports.get_assigned_orders_previous(request.user)
    previous_assigned_orders_commission_total = reports.get_assigned_order_totals_commission_previous(request.user)
    previous_total_commission = reports.total_commission_previous(request.user)
    previous_salary = reports.get_salary(request.user)
    previous_gross_salary = reports.carpenter_gross_salary_previous(request.user)

    # getting the month name from its number
    month = calendar.month_name[reports.current_month()['month']]
    year = reports.current_month()['year']
    previous_month = calendar.month_name[reports.previous_month()['pre_month']]
    previous_year = reports.previous_month()['year']
    return render(request, 'reports/carpenter_report.html', locals())


@login_required(login_url='/')
def show_monthly_summary(request):
    # current month summary
    salary_totals = reports.get_salary_totals()
    orders_totals = reports.get_orders_totals_current()
    commission_totals = reports.get_commissions_grand_totals_current()
    damage_fee_totals = reports.get_total_tool_damage_fees_current()
    storage_fee_totals = reports.get_total_storage_fees_current()
    lending_fee_totals = reports.get_total_lending_fees_current()
    lent_tools = reports.get_current_returned_tools()
    orders_with_storage_fee = reports.get_orders_with_storage_fee_current()
    damaged_tools = reports.get_damaged_tools_current()
    carpenter_profiles = reports.get_carpenter_profiles()
    complete_orders = reports.get_all_complete_orders_current()
    carpenter_commission_totals = reports.get_carpenter_commissions_subtotals_current()
    temp_carpenter_commission_totals = reports.get_temp_carpenter_commissions_subtotals_current()

    # previous month summary
    previous_salary_totals = reports.get_salary_totals()
    previous_orders_totals = reports.get_orders_totals_previous()
    previous_commission_totals = reports.get_commissions_grand_totals_previous()
    previous_damage_fee_totals = reports.get_total_tool_damage_fees_previous()
    previous_storage_fee_totals = reports.get_total_storage_fees_previous()
    previous_lending_fee_totals = reports.get_total_lending_fees_previous()
    previous_lent_tools = reports.get_previous_returned_tools()
    previous_orders_with_storage_fee = reports.get_orders_with_storage_fee_previous()
    previous_damaged_tools = reports.get_damaged_tools_previous()
    previous_carpenter_profiles = reports.get_carpenter_profiles()
    previous_complete_orders = reports.get_all_complete_orders_previous()
    previous_carpenter_commission_totals = reports.get_carpenter_commissions_subtotals_previous()
    previous_temp_carpenter_commission_totals = reports.get_temp_carpenter_commissions_subtotals_previous()

    # getting the month name from its number
    month = calendar.month_name[reports.current_month()['month']]
    year = reports.current_month()['year']
    previous_month = calendar.month_name[reports.previous_month()['pre_month']]
    previous_year = reports.previous_month()['year']
    return render(request, 'reports/monthly_report.html', locals())
