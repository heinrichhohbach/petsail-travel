# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .forms import AdPostForm
from django import forms


# Create your tests here.
class AdTest(TestCase):
    def test_ad_create(self):
        form = AdPostForm({
            'subject': 'This is a test Subject',
            'ad_summary': 'This is an ad summary',
            'description': 'This is an ad description',
            'start_date': '2018-01-01',
            'end_date': '2018-01-01',
            'ad_price': '55.55'
        })
        self.assertTrue(form.is_valid())

    def test_ad_create_no_subject(self):
        form = AdPostForm({
            'ad_summary': 'This is an ad summary',
            'description': 'This is an ad description',
            'start_date': '2018-01-01',
            'end_date': '2018-01-01',
            'ad_price': '55.55'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a subject",
                                 form.full_clean())

    def test_ad_create_no_summary(self):
        form = AdPostForm({
            'subject': 'This is a test Subject',
            'description': 'This is an ad description',
            'start_date': '2018-01-01',
            'end_date': '2018-01-01',
            'ad_price': '55.55'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a summary",
                                 form.full_clean())

    def test_ad_create_no_description(self):
        form = AdPostForm({
            'subject': 'This is a test Subject',
            'ad_summary': 'This is an ad summary',
            'start_date': '2018-01-01',
            'end_date': '2018-01-01',
            'ad_price': '55.55'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a description",
                                 form.full_clean())

    def test_ad_create_no_start(self):
        form = AdPostForm({
            'subject': 'This is a test Subject',
            'ad_summary': 'This is an ad summary',
            'description': 'This is an ad description',
            'end_date': '2018-01-01',
            'ad_price': '55.55'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a start date",
                                 form.full_clean())

    def test_ad_create_no_end(self):
        form = AdPostForm({
            'subject': 'This is a test Subject',
            'ad_summary': 'This is an ad summary',
            'description': 'This is an ad description',
            'start_date': '2018-01-01',
            'ad_price': '55.55'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter an end date",
                                 form.full_clean())

    def test_ad_create_no_price(self):
        form = AdPostForm({
            'subject': 'This is a test Subject',
            'ad_summary': 'This is an ad summary',
            'description': 'This is an ad description',
            'start_date': '2018-01-01',
            'end_date': '2018-01-01'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a price",
                                 form.full_clean())