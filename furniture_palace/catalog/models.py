from django.db import models


# Create your models here.
class Furniture(models.Model):
    # bed options
    double = 'double'
    single = 'single'
    double_decker = 'double_decker'
    # table options
    coffee = 'Coffee Table'
    dinning = 'Dinning Table'
    kitchen = 'Kitchen Table'
    office_table = 'Office Table'
    # seat options
    arm = 'Arm Chair'
    classroom = 'Classroom Chairs'
    office_chair = 'Office Chairs'
    benches = 'Benches'

    furniture_choices = (
        (double, 'Double Bed'),
        (single, 'Single Bed'),
        (double_decker, 'Double Decker'),
        (coffee, 'Coffee Table'),
        (dinning, 'Dinning Table'),
        (kitchen, 'Kitchen Table'),
        (office_table, 'Office Table'),
        (arm, 'Arm Chair'),
        (classroom, 'Classroom Chair'),
        (office_chair, 'Office Chair'),
        (benches, 'Benches'),
    )
    furniture_name = models.CharField(
        max_length=50,
        choices=furniture_choices,
        default='Choose',
    )

    furniture_category_choices = (
        ('bed', 'Beds'),
        ('seat', 'Seats'),
        ('table', 'Tables'),
    )

    furniture_category = models.CharField(max_length=200,
                                          choices=furniture_category_choices,
                                          default='Choose',
                                          )

    def __str__(self):
        return self.furniture_name


class Tool(models.Model):
    tool_name = models.CharField(max_length=250)
    lending_rate_per_day = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.tool_name


class Material(models.Model):
    nails, varnish, glass, fabrics, cushions = 'nails', 'varnish', 'glass', 'fabrics', 'cushions'
    material_choices = (
        (nails, 'Nails'),
        (varnish, 'Varnish'),
        (glass, 'Glass'),
        (fabrics, 'Fabrics'),
        (cushions, 'Cushions'),
    )

    material_name = models.CharField(max_length=100, choices=material_choices, default=nails)

    per_unit_price = models.FloatField()

    def __str__(self):
        return self.material_name
