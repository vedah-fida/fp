# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_orderpayment_storage_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.FloatField(null=True),
        ),
    ]
