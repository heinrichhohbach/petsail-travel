# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_dash', '0007_ad_ad_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='ad_summary',
            field=models.CharField(default='', max_length=255),
        ),
    ]
