from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from catalog.models import Furniture
from order.order import *
from order.order_payments import *
from django.contrib.auth.models import User
from accounts.models import Customer, TempCarpenter


# Create your views here.
@login_required(login_url='/')
def make_order_page(request):
    furniture = Furniture.objects.all()
    customers = Customer.objects.all()
    return render(request, 'order/order_make.html', locals())


@login_required(login_url='/')
def make_order(request):
    # data for order
    order_name = request.POST['order_name']
    quantity = float(request.POST['quantity'])
    order_completion_date = request.POST['order_completion_date']
    customer = int(request.POST['customer'])

    # data for order payment
    deposit = float(request.POST['deposit'])

    # getting the material price of the order and hence the order price
    furniture = Furniture.objects.get(furniture_name=order_name)
    order_price = (float(furniture.material_price) * 1.7) * quantity

    # create and save order

    new_order_id = save_order_and_return_id(customer, order_name, quantity, order_price, deposit)
    order = get_order(new_order_id)
    order_payment = get_order_payment(new_order_id)
    return render(request, 'order/order_info.html', locals())


@login_required(login_url='/')
def change_complete_status(request):
    order_number = request.POST['order_id']
    status = request.POST['order_status']
    change_order_status(order_number, status)
    orders = get_started_orders()
    customers = Customer.objects.all()
    carpenters = User.objects.all().exclude(username="wolf")
    msg = 'Complete status for order with order id ' + order_number + ' successfully changed.'
    return render(request, 'order/order_view.html', locals())


@login_required(login_url='/')
def view_all_orders(request):
    orders_list = get_started_orders()
    paginator = Paginator(orders_list, 2)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    customers = Customer.objects.all()
    carpenters = User.objects.all().exclude(username="wolf")
    return render(request, 'order/order_view.html', locals())


@login_required(login_url='/')
def search_order(request):
    search_query = request.POST['query']
    search_field = request.POST['search_field']
    customers = Customer.objects.all()
    carpenters = User.objects.all().exclude(username="wolf")
    orders = search_for_orders(search_query, search_field)
    return render(request, 'order/order_view.html', locals())


@login_required(login_url='/')
def view_orders_for_customer(request):
    customer_id = request.POST['customer_id']
    orders = get_orders_for(customer_id)
    customers = Customer.objects.all()
    carpenters = User.objects.all().exclude(username="wolf")
    return render(request, 'order/order_view.html', locals())


@login_required(login_url='/')
def view_complete_status_orders(request):
    status = request.POST['status']
    if status == "complete":
        orders = get_complete_orders()
        customers = Customer.objects.all()
        carpenters = User.objects.all().exclude(username="wolf")
        return render(request, 'order/order_view.html', locals())
    elif status == "incomplete":
        orders = get_incomplete_orders()
        customers = Customer.objects.all()
        carpenters = User.objects.all().exclude(username="wolf")
        return render(request, 'order/order_view.html', locals())
    else:
        orders = get_started_orders()
        customers = Customer.objects.all()
        carpenters = User.objects.all().exclude(username="wolf")
        return render(request, 'order/order_view.html', locals())


@login_required(login_url='/')
def carpenter_orders(request):
    carpenter_id = request.POST['carpenter_id']
    orders = get_carpenter_orders(carpenter_id)
    customers = Customer.objects.all()
    carpenters = User.objects.all().exclude(username="wolf")
    return render(request, 'order/order_view.html', locals())


@login_required(login_url='/')
def assign_order_page(request):
    orders_list = get_unassigned_orders()
    paginator = Paginator(orders_list, 3)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    user = request.user
    temporary_carpenters = TempCarpenter.objects.all()
    active_orders = Order.objects.filter(carpenter=user,
                                         complete_status=False,
                                         temp_carpenter=None)

    return render(request, 'order/order_assign.html', locals())


@login_required(login_url='/')
def take_order(request):
    # get user
    carpenter = request.user

    # check if carpenter has more than 4 already assigned to him/her
    if carpenter_active_orders(carpenter) < 4:
        order_id = request.POST['order_id']
        assign_order_self(carpenter, order_id)
        msg = "You have taken the order with id " + order_id
        orders = get_unassigned_orders()
        temporary_carpenters = TempCarpenter.objects.all()
        styling = "card-panel green accent-4"
        return render(request, 'order/order_assign.html', locals())
    else:
        msg = "Currently, you have the maximum allowed active orders."
        orders = get_unassigned_orders()
        temporary_carpenters = TempCarpenter.objects.all()
        styling = "card-panel red lighten-1"
        return render(request, 'order/order_assign.html', locals())


@login_required(login_url='/')
def assign_order(request):
    order_id = request.POST['order_id']
    temp_carpenter_id = request.POST['temp_carpenter']
    carpenter = request.user
    assign_order_to(temp_carpenter_id, carpenter, order_id)
    msg = "You have successfully assigned the order."
    orders = get_unassigned_orders()
    temporary_carpenters = TempCarpenter.objects.all()
    styling = "card-panel green accent-4"
    return render(request, 'order/order_assign.html', locals())


@login_required(login_url='/')
def edit_order(request):
    order_id = request.POST['order_id']
    order = Order.object.get(id=order_id)
    customers = Customer.objects.all()
    return render(request, 'order/order_info.html', locals())


@login_required(login_url='/')
def delete_order(request):
    pass


@login_required(login_url='/')
def show_payment_list(request):
    orders_payment_list = get_undelivered_order_payments()
    paginator = Paginator(orders_payment_list, 6)
    page = request.GET.get('page')
    try:
        order_payments = paginator.page(page)
    except PageNotAnInteger:
        order_payments = paginator.page(1)
    except EmptyPage:
        order_payments = paginator.page(paginator.num_pages)

    return render(request, 'order/order_payments_list.html', locals())


@login_required(login_url='/')
def show_order_payment(request):
    order = request.POST['order']
    order_payment = get_order_payment(order)
    return render(request, 'order/order_payment.html', locals())


@login_required(login_url='/')
def update_order(request):
    order_id = request.POST['order']
    paid_amount = float(request.POST['paid_amount'])
    delivery = request.POST['delivery']
    update_order_payment(order_id, paid_amount, delivery)

    msg = "Update was made successfully."
    order_payments = get_undelivered_order_payments()
    return render(request, 'order/order_payments_list.html', locals())
