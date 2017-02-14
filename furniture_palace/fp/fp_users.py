from .models import Carpenter


def carpenter_is_valid(email, password):
    try:
        carpenter = Carpenter.objects.get(carpenter_email=email)
        if carpenter.carpenter_password == password:
            print("password is correct")
            return True
        else:
            print('password is incorrect')
            return False
    except Carpenter.DoesNotExist:
        print('the carpenter is not in the database')
