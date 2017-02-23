from django.shortcuts import render
from catalog.models import Furniture
from accounts.models import Customer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def get_furniture(request):
    order_name = request.POST('order_name')
    chosen_furniture = Furniture.objects.get(furniture_name=order_name)
    furniture = Furniture.objects.all()
    customers = Customer.objects.all()
    return render(request, 'order/order_make.html', locals())
