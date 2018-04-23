# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from checkout.forms import CheckoutForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.conf import settings
import datetime
import stripe

from merchant_dash.models import Ad

stripe.api_key = settings.STRIPE_SECRET
checkout_global = 0


def checkoutview(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(str(checkout_global).replace('.', '')),
                    currency="GBP",
                    description=form.cleaned_data['checkout_email'],
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    payment = form.save(commit=False)
                    payment.customer_id = request.user
                    payment.payment_amount = checkout_global
                    payment.payment_date = datetime.date.today()
                    payment.save()
                    messages.success(request, "Your Payment was successful")
                    return redirect(reverse('profile'))
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = CheckoutForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'Check': checkout_global}
    args.update(csrf(request))

    return render(request, 'checkout/sale_checkout.html', args)


def checkout_view_init(request):
    checkout_test = request.META.get('HTTP_REFERER')
    checkout_test2 = checkout_test.split('/')[4]
    checkout_ad = Ad.objects.get(id=checkout_test2)
    checkout_ad2 = checkout_ad.ad_price
    global checkout_global
    checkout_global = checkout_ad2
    return redirect('checkout')
