# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
from tinymce.models import HTMLField
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Ad(models.Model):
    subject = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    ad_summary = models.CharField(max_length=255, default='')
    description = RichTextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    published = models.CharField(max_length=3, default='Yes')
    ad_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.subject
