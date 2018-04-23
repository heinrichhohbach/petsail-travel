# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .forms import CheckoutForm
from django import forms


# Create your tests here.
class CheckoutTest(TestCase):

    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)

    def test_checkout_form(self):
        form = CheckoutForm({
            'checkout_email': 'test@test.com',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2020',
            'stripe_id': 'tok_1CJlcvKIrAmx06SPklWNzsEb'

        })
        self.assertTrue(form.is_valid())

    def test_checkout_form_no_email(self):
        form = CheckoutForm({
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2020',
            'stripe_id': 'tok_1CJlcvKIrAmx06SPklWNzsEb'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_checkout_form_no_credit(self):
        form = CheckoutForm({
            'checkout_email': 'test@test.com',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2020',
            'stripe_id': 'tok_1CJlcvKIrAmx06SPklWNzsEb'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your credit card number",
                                 form.full_clean())

    def test_checkout_form_no_cvv(self):
        form = CheckoutForm({
            'checkout_email': 'test@test.com',
            'credit_card_number': '4242424242424242',
            'expiry_month': '2',
            'expiry_year': '2020',
            'stripe_id': 'tok_1CJlcvKIrAmx06SPklWNzsEb'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your CVV code",
                                 form.full_clean())

    def test_checkout_form_no_month(self):
        form = CheckoutForm({
            'checkout_email': 'test@test.com',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_year': '2020',
            'stripe_id': 'tok_1CJlcvKIrAmx06SPklWNzsEb'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your expiry month",
                                 form.full_clean())

    def test_checkout_form_no_year(self):
        form = CheckoutForm({
            'checkout_email': 'test@test.com',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'stripe_id': 'tok_1CJlcvKIrAmx06SPklWNzsEb'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your expiry year",
                                 form.full_clean())

    def test_checkout_form_no_stripe(self):
        form = CheckoutForm({
            'checkout_email': 'test@test.com',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2020'

        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Card payment was not successful.",
                                 form.full_clean())
