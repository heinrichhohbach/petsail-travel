# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ContactUs(models.Model):
    contact_title = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    query_type = models.CharField(max_length=255)
    query_text = models.TextField()

    def __str__(self):
        return self.contact_title
