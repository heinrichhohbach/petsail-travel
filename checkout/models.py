# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class CustomerSale(models.Model):
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='customerTag')
    stripe_id = models.CharField(max_length=40, default='')
    checkout_email = models.EmailField(default='')
