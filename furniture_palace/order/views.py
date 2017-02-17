from django.shortcuts import render
from order.forms import OrderForm
from order.order import get_minimum_price
from order.models import Order
from catalog.models import Material
from accounts.models import Customer


# Create your views here.

def order_page(request):
    form = OrderForm()
    materials = Material.objects.all()
    return render(request, 'order/make_order.html', locals())


def make_order(request):
    # data for order
    order_name = request.POST['order_name']
    order_completion_date = request.POST['order_completion_date']
    customer = int(request.POST['customer'])

    # data for materials
    nails = float(request.POST['nails'])
    fabrics = float(request.POST['fabrics'])
    cushions = float(request.POST['cushions'])
    glass = float(request.POST['glass'])
    varnish = float(request.POST['varnish'])

    # create order
    new_order = Order()
    new_order.order_name = order_name
    new_order.order_completion_date = order_completion_date
    new_order.customer = Customer.objects.get(id=customer)
    new_order.order_price = get_minimum_price(nails, varnish, glass, fabrics, cushions)

    new_order.save()

    msg = 'Order was created successfully.'
    form = OrderForm()
    materials = Material.objects.all()
    return render(request, 'order/make_order.html', locals())
