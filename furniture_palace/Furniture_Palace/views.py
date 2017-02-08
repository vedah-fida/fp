from django.shortcuts import render, HttpResponse
from .models import Customer


# login logic
def home(request):
    return render(request, 'Furniture_Palace/home.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pword']
        try:
            customer = Customer.objects.get(customer_email=email)
        except Customer.DoesNotExist:
            return HttpResponse("<h1>Unsuccesful Login</h1>")

        if customer:
            if customer.customer_password == password:
                return render(request, 'Furniture_Palace/success.html')
            else:
                return HttpResponse("<h1>Unsuccesful Login</h1>")
