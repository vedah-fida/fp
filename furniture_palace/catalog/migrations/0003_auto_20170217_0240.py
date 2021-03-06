# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-17 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_furniture_furniture_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='furniture_name',
            field=models.CharField(choices=[('double', 'Double Bed'), ('single', 'Single Bed'), ('double_decker', 'Double Decker'), ('Coffee Table', 'Coffee Table'), ('Dinning Table', 'Dinning Table'), ('Kitchen Table', 'Kitchen Table'), ('Office Table', 'Office Table'), ('Arm Chair', 'Arm Chair'), ('Classroom Chairs', 'Classroom Chair'), ('Office Chairs', 'Office Chair'), ('Benches', 'Benches')], default='Choose', max_length=50),
        ),
        migrations.AlterField(
            model_name='material',
            name='per_unit_price',
            field=models.FloatField(),
        ),
    ]
