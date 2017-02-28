from catalog.models import Furniture
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def get_furniture(request):
    furniture = Furniture.objects.all()
    serialized_furniture = serializers.serialize('json', furniture)
    return JsonResponse(serialized_furniture, safe=False)
