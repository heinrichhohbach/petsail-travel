# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages


# Create your views here.
def new_contact(request):
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()
            messages.success(request, "Thanks! Someone will get back to you soon!")
            contact_form = ContactUsForm()
    else:
        contact_form = ContactUsForm()
    return render(request, 'General Pages/contact_us.html', {'form': contact_form})
