from django.shortcuts import render, HttpResponseRedirect
from django.core import urlresolvers
from django.contrib.auth import authenticate, login, logout
from accounts.forms import CustomerForm
from accounts.models import Customer
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
        carpenter = request.user.username
        return render(request, 'accounts/carpenter_home.html', locals())
    else:
        error_msg = "Either the username or password you typed is incorrect."
        return render(request, 'accounts/index.html', {'msg': error_msg})


def register_customer_page(request):
    register_form = CustomerForm()
    return render(request, 'accounts/register_customer.html', locals())


def register_customer(request):
    postdata = request.POST.copy()
    customer_email = postdata.get('customer_email', '')
    if customer_exists(customer_email):
        register_form = CustomerForm()
        error_msg = 'Customer already exists.'
        return render(request, 'accounts/register_customer.html', locals())
    else:
        customer_name = postdata.get('customer_name', '')
        customer_tel_no = postdata.get('customer_tel_no', '')
        customer_address = postdata.get('customer_address', '')
        customer_class = postdata.get('customer_class', '')

        new_customer = Customer()
        new_customer.customer_name = customer_name
        new_customer.customer_email = customer_email
        new_customer.customer_address = customer_address
        new_customer.customer_tel_no = customer_tel_no
        new_customer.customer_class = customer_class

        new_customer.save()

        register_form = CustomerForm()
        success = 'Customer successfully registered.'
        return render(request, 'accounts/register_customer.html', locals())


def logout_carpenter(request):
    logout(request)
    url = urlresolvers.reverse('accounts:index')
    return HttpResponseRedirect(url)
