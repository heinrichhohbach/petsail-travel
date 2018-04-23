# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import User
import arrow
import json
from merchant_dash.models import Ad
from checkout.models import CustomerSale


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_merchant = request.POST.get('merchantstatus')
            user.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1')
                                     )

            if user.is_merchant == "Yes":
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('merchant'))
            elif user.is_merchant == "No":
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "Unable to register you at this time.")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'accounts/register.html', args)


@login_required(login_url='/login/')
def profile(request):
    current_user = request.user
    ads_p = CustomerSale.objects.filter(customer_id=current_user.id)
    return render(request, 'accounts/profile.html', {'Customer': ads_p})


@login_required(login_url='/login/')
def merchantprofile(request):
    current_user = request.user
    ads = Ad.objects.filter(user=current_user.id)
    return render(request, 'accounts/merchant_profile.html',
                  {'Ad': ads})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                if user.is_merchant == 'Yes':
                    return redirect(reverse('merchant'))
                else:
                    return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was incorrect")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')
