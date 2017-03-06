from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from reports import reports
from catalog.catalog import get_returned_lent_tools


@login_required(login_url='/')
def show_carpenter_summary(request):
    carpenter_orders = reports.get_carpenter_orders(request.user)
    carpenter_orders_commission_total = reports.get_carpenter_order_totals_commission(request.user)
    assigned_orders = reports.get_assigned_orders(request.user)
    assigned_orders_commission_total = reports.get_assigned_order_totals_commission(request.user)
    total_commission = reports.total_commission(request.user)
    salary = reports.get_salary(request.user)
    gross_salary = reports.carpenter_gross_salary(request.user)
    orders_commission = float(0.02)
    assigned_order_commission = float(0.01)
    return render(request, 'reports/carpenter_report.html', locals())


@login_required(login_url='/')
def show_monthly_summary(request):
    # lending_fees(pending)
    # delivery_fees(pending)
    salary_totals = reports.get_salary_totals()
    orders_totals = reports.get_orders_totals()
    commission_totals = reports.get_commissions_grand_totals()
    damage_fee_totals = reports.get_total_tool_damage_fees()
    storage_fee_totals = reports.get_total_storage_fees()
    lending_fee_totals = reports.get_total_lending_fees()

    lent_tools = get_returned_lent_tools()
    orders_with_storage_fee = reports.get_orders_with_storage_fee()
    damaged_tools = reports.get_damaged_tools()
    carpenter_profiles = reports.get_carpenter_profiles()
    complete_orders = reports.get_all_complete_orders()
    carpenter_commission_totals = reports.get_carpenter_commissions_subtotals()
    temp_carpenter_commission_totals = reports.get_temp_carpenter_commissions_subtotals()
    return render(request, 'reports/monthly_report.html', locals())
