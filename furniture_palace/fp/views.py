from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.core.urlresolvers import reverse
from .fp_users import carpenter_is_valid


def home(request):
    url = reverse('carpenter_login_page')
    return HttpResponseRedirect(url)


def carpenter_login_page(request):
    return render(request, 'fp/carpenter_login.html')


def carpenter_login(request):
    postdata = request.POST.copy()
    email = postdata.get('email', '')
    password = postdata.get('pword', '')
    if carpenter_is_valid(email, password):
        return render(request, 'fp/carpenter_home.html')
    else:
        return HttpResponse("<h1>Unsuccessful Login.</h1>")


def lend_tool(request):
    # some code for lending tools
    return render(request, 'fp/lend_tool.html')


def register_customer(request):
    # some code for registering customer
    return render(request, 'fp/register_customer.html')


def payment_summary(request):
    # some code for payment summary
    return render(request, 'fp/carpenter_payments.html')


def make_order(request):
    # some code for making order
    return render(request, 'fp/make_order.html')


def logout(request):
    url = reverse('carpenter_login_page')
    return HttpResponseRedirect(url)
