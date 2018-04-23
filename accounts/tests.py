# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm, UserLoginForm
from django import forms
from django.conf import settings


# Create your tests here.
class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'merchantstatus': 'Yes'
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1',
            'merchantstatus': 'Yes'
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_fails_with_empty_password1(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password2': 'letmein1',
            'merchantstatus': 'Yes'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_fails_with_empty_password2(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'merchantstatus': 'Yes'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
            'merchantstatus': 'Yes'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())
