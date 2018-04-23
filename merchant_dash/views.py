# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Ad
from .forms import AdPostForm
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def ad_detail(request, id):
    ad = get_object_or_404(Ad, pk=id)
    return render(request, "merchant_dash/addetail.html", {'post': ad})


@login_required(login_url='/login/')
def new_ad(request):
    if request.method == "POST":
        ad_form = AdPostForm(request.POST)
        if ad_form.is_valid():
            ad = ad_form.save(commit=False)
            ad.user = request.user
            ad.published = "Yes"
            ad.save()
            return redirect(ad_detail, ad.pk)
    else:
        ad_form = AdPostForm()
    return render(request, 'merchant_dash/adpostform.html', {'form': ad_form})


def all_ads(request):
    ads = Ad.objects.all()
    return render(request, 'Ads/ad_listing.html',
                  {'Ad': ads})


@login_required
def delete_post(request, ad_id):
    post = get_object_or_404(Ad, pk=ad_id)
    post.delete()

    messages.success(request, "Your post was deleted!")

    return redirect('merchant')


@login_required(login_url='/login/')
def edit_ad(request, ad_id=None):
    item = get_object_or_404(Ad, id=ad_id)
    form = AdPostForm(request.POST or None, instance=item)
    if form.is_valid():
        ad = form.save(commit=False)
        ad.user = request.user
        ad.published = "Yes"
        ad.save()
        return redirect(ad_detail, ad.pk)
    return render(request, 'merchant_dash/adpostform.html', {'form': form})
