# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .forms import ContactUsForm
from django import forms


# Create your tests here.
class ContactUsTest(TestCase):

    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)

    def test_contact_form(self):
        form = ContactUsForm({
            'contact_title': 'Subject Title',
            'contact_name': 'heinrich',
            'contact_email': 'test@test.com',
            'query_type': 'Merchant Problems',
            'query_text': 'This is a query'

        })
        self.assertTrue(form.is_valid())

    def test_contact_form_no_title(self):
        form = ContactUsForm({
            'contact_name': 'heinrich',
            'contact_email': 'test@test.com',
            'query_type': 'Merchant Problems',
            'query_text': 'This is a query'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a Title",
                                 form.full_clean())

    def test_contact_form_no_name(self):
        form = ContactUsForm({
            'contact_title': 'Subject Title',
            'contact_email': 'test@test.com',
            'query_type': 'Merchant Problems',
            'query_text': 'This is a query'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your Name",
                                 form.full_clean())

    def test_contact_form_no_email(self):
        form = ContactUsForm({
            'contact_title': 'Subject Title',
            'contact_name': 'heinrich',
            'query_type': 'Merchant Problems',
            'query_text': 'This is a query'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your Email.",
                                 form.full_clean())

    def test_contact_form_no_type(self):
        form = ContactUsForm({
            'contact_title': 'Subject Title',
            'contact_name': 'heinrich',
            'contact_email': 'test@test.com',
            'query_text': 'This is a query'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please choose a Query Type",
                                 form.full_clean())

    def test_contact_form_no_text(self):
        form = ContactUsForm({
            'contact_title': 'Subject Title',
            'contact_name': 'heinrich',
            'contact_email': 'test@test.com',
            'query_type': 'Merchant Problems'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a Query Text",
                                 form.full_clean())
