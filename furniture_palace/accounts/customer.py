from accounts.models import Customer


# confirm if customer exists in the database
def customer_exists(email):
    try:
        customer = Customer.objects.get(customer_email=email)
        if customer is not None:
            return True
        else:
            return False
    except Customer.DoesNotExist:
        return False


def save_customer(customer_name, customer_email, customer_tel_no, customer_address, physical_address):
    # create new customer
    new_customer = Customer()

    # assign values to the new customer
    new_customer.customer_name = customer_name
    new_customer.customer_email = customer_email
    new_customer.customer_address = customer_address
    new_customer.customer_physical_address = physical_address
    new_customer.customer_tel_no = customer_tel_no

    # save new customer
    new_customer.save()


# update customer record
def update_customer_with_details(name, email, tel_no, address, physical_address):
    # get customer to be updated
    customer_to_update = Customer.objects.get(customer_email=email)

    # update customer with new values
    customer_to_update.customer_name = name
    customer_to_update.customer_email = email
    customer_to_update.customer_tel_no = tel_no
    customer_to_update.customer_address = address
    customer_to_update.customer_physical_address = physical_address

    # save updated values
    customer_to_update.save()


def get_all_customers():
    # get all customers
    customers = Customer.objects.all()
    # return all customers
    return customers


def get_customer_with_id(customer_id):
    # get customer with the id in parameter
    customer = Customer.objects.get(id=customer_id)
    # return the customer with the id
    return customer
