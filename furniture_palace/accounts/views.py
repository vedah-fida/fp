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
        url = urlresolvers.reverse('orders:all_orders')
        return HttpResponseRedirect(url)
    else:
        error_msg = "Incorrect username or password. Please try again."
        error_class = "card-panel red lighten-1"
        return render(request, 'accounts/index.html', locals())


def register_customer_page(request):
    return render(request, 'accounts/customer_register.html', locals())


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
        return render(request, 'accounts/customer_register.html', locals())
    else:
        save_customer(customer_name, customer_email, customer_tel_no, customer_address, customer_physical_address)
        success = 'Customer successfully registered.'
        return render(request, 'accounts/customer_register.html', locals())


def view_customers(request):
    customers = get_all_customers()
    return render(request, 'accounts/customer_view.html', {'customers': customers})


def get_customer(request):
    customer_id = request.POST['customer_id']
    customer = get_customer_with_id(customer_id)
    return render(request, 'accounts/customer_update.html', {'customer': customer})


def update_customer(request):
    customer_id = request.POST['customer_id']
    customer_name = request.POST['customer_name']
    customer_email = request.POST['customer_email']
    customer_tel_no = request.POST['customer_tel']
    customer_address = request.POST['customer_address']
    customer_physical_address = request.POST['physical_address']

    update_customer_with_details(customer_id, customer_name, customer_email, customer_tel_no, customer_address, customer_physical_address)
    msg = "Customer edit successfull."
    customers = get_all_customers()
    return render(request, 'accounts/customer_view.html', locals())


def logout_carpenter(request):
    logout(request)
    url = urlresolvers.reverse('accounts:index')
    return HttpResponseRedirect(url)
