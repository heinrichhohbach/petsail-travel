# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from checkout.forms import CheckoutForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET


def checkoutview(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=999,
                    currency="USD",
                    description=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    payment = form.save(commit=False)
                    payment.customer_id = request.user.id
                    payment.save()
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = CheckoutForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'checkout/sale_checkout.html', args)
