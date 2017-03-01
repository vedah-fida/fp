from django.shortcuts import render
from reports import reports
from accounts.models import Profile



# Create your views here.
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
