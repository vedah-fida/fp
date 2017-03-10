from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect
from django.core import urlresolvers
from django.contrib.auth import authenticate, login, logout
from accounts.customer import *
from accounts.customer import customer_exists


def landing_page(request):
    return render(request, 'accounts/index.html')


def login_carpenter(request):
    logout(request)
    postdata = request.POST.copy()
    user_name = postdata.get('username', '')
    password = postdata.get('password', '')
    user = authenticate(username=user_name, password=password)
    if user is not None and user.is_active:
        login(request, user)
        url = urlresolvers.reverse('orders:active_orders')
        return HttpResponseRedirect(url)
    else:
        error_msg = "Incorrect username or password. Please try again."
        error_class = "card-panel red lighten-1"
        return render(request, 'accounts/index.html', locals())


@login_required(login_url='/')
def register_customer_page(request):
    return render(request, 'accounts/customer_register.html', locals())


@login_required(login_url='/')
def register_customer(request):
    # get data from the form in customer_register.html file
    postdata = request.POST.copy()
    customer_name = postdata.get('customer_name', '')
    customer_email = postdata.get('customer_email', '')
    customer_tel_no = postdata.get('customer_tel', '')
    customer_address = postdata.get('customer_address', '')
    customer_physical_address = postdata.get('physical_address', '')

    # check if the customer exists or not and throw an error or save the customer
    if customer_exists(customer_email):
        error_msg = 'Customer already exists.'
        error_styling = 'card-panel red lighten-1'
        return render(request, 'accounts/customer_register.html', locals())
    else:
        save_customer(customer_name, customer_email, customer_tel_no, customer_address, customer_physical_address)
        success = 'Customer successfully registered.'
        success_styling = 'card-panel teal lighten-2'
        return render(request, 'accounts/customer_register.html', locals())


@login_required(login_url='/')
def view_customers(request):
    customers_list = get_all_customers()
    paginator = Paginator(customers_list, 5)
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)
    return render(request, 'accounts/customer_view.html', {'customers': customers})


@login_required(login_url='/')
def get_customer(request):
    customer_id = request.POST['customer_id']
    customer = get_customer_with_id(customer_id)
    return render(request, 'accounts/customer_update.html', {'customer': customer})


@login_required(login_url='/')
def update_customer(request):
    customer_id = request.POST['customer_id']
    customer_name = request.POST['customer_name']
    customer_email = request.POST['customer_email']
    customer_tel_no = request.POST['customer_tel']
    customer_address = request.POST['customer_address']
    customer_physical_address = request.POST['physical_address']

    update_customer_with_details(customer_id, customer_name, customer_email, customer_tel_no, customer_address,
                                 customer_physical_address)
    msg = "Customer with id "+customer_id+" has been updated."
    success_styling = 'card-panel teal lighten-2'
    customers = get_all_customers()
    return render(request, 'accounts/customer_view.html', locals())


@login_required(login_url='/')
def search_customer(request):
    query = request.POST['query']
    customers = search_for_customer(query)
    return render(request, 'accounts/customer_view.html', locals())


def logout_carpenter(request):
    logout(request)
    url = urlresolvers.reverse('accounts:index')
    return HttpResponseRedirect(url)
