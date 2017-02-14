from django.db import models


# models
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=254)
    customer_tel_no = models.CharField(max_length=100)
    customer_address = models.TextField()

    # customer type according to order made
    gold, silver = 'Gold', 'Silver'
    customer_type_choices = (
        (gold, 'GOLD'),
        (silver, 'SILVER'),
    )
    customer_class = models.CharField(
        max_length=15,
        choices=customer_type_choices,
        default=silver,
    )

    def __str__(self):
        return self.customer_name


class Carpenter(models.Model):
    carpenter_name = models.CharField(max_length=100)
    carpenter_email = models.EmailField(max_length=254)
    carpenter_password = models.CharField(max_length=100)
    carpenter_tel_no = models.CharField(max_length=100)
    carpenter_address = models.CharField(max_length=100)
    carpenter_salary = models.DecimalField(max_digits=9, decimal_places=2)
    commission = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.carpenter_name


class TempCarpenter(models.Model):
    temp_carpenter_name = models.CharField(max_length=100)
    order = models.ForeignKey('Order')
    carpenter = models.ForeignKey('Carpenter')

    def __str__(self):
        return self.temp_carpenter_name


class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_complete = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=20, decimal_places=2)
    order_completion_date = models.DateField()
    customer = models.ForeignKey('Customer', null=False, unique=False)
    carpenter = models.ForeignKey('Carpenter', null=True, unique=False)

    def __str__(self):
        return self.order_name


class Material(models.Model):
    nails, varnish, glass, fabrics, cushions = 'nails', 'varnish', 'glass', 'fabrics', 'cushions'
    material_choices = (
        (nails, 'nails'),
        (varnish, 'varnish'),
        (glass, 'glass'),
        (fabrics, 'fabrics'),
        (cushions, 'cushions'),
    )

    material_name = models.CharField(max_length=100, choices=material_choices, default=nails)

    material_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.material_name


class Tool(models.Model):
    tool_name = models.CharField(max_length=250)
    lent = models.BooleanField(default=False)
    lending_rate_per_day = models.DecimalField(max_digits=7, decimal_places=2 )
    temp_carpenter = models.ForeignKey('TempCarpenter', null=True, unique=False)

    def __str__(self):
        return self.tool_name


class Bed(models.Model):
    double = 'double'
    single = 'single'
    double_decker = 'double_decker'
    bed_categories = (
        (double, 'DOUBLE'),
        (single, 'SINGLE'),
        (double_decker, 'DOUBLE DECKER'),
    )

    category = models.CharField(
        max_length=50,
        choices=bed_categories,
        default=single,
    )

    bed_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.category


class Table(models.Model):
    coffee = 'Coffee Table'
    dinning = 'Dinning Table'
    kitchen = 'Kitchen Table'
    office = 'Office Table'

    table_categories = (
        (coffee, 'Coffee Table'),
        (dinning, 'Dinning Table'),
        (kitchen, 'Kitchen Table'),
        (office, 'Office Table'),
    )

    category = models.CharField(
        max_length=50,
        choices=table_categories,
        default=coffee,
    )

    table_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.category


class Seat(models.Model):
    arm = 'Arm Chair'
    classroom = 'Classroom Chairs'
    office = 'Office Chairs'
    benches = 'Benches'

    seat_categories = (
        (arm, 'Arm Chair'),
        (classroom, 'Classroom Chairs'),
        (office, 'Office Chairs'),
        (benches, 'Benches'),
    )

    category = models.CharField(
        max_length=50,
        choices=seat_categories,
        default=office,
    )

    seat_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.category
