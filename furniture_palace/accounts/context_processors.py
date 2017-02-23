from catalog.models import Furniture


def username_processor(request):
    username = request.user.username
    return {'username': username}


def furniture_processor(request):
    furniture = Furniture.objects.all()
    return {'furniture': furniture}
