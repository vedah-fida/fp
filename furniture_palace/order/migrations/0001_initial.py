# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-16 14:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20170216_1427'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=100)),
                ('order_complete', models.BooleanField(default=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('order_completion_date', models.DateField()),
                ('carpenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
                ('temp_carpenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.TempCarpenter')),
            ],
        ),
    ]
