# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20180415_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersale',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
