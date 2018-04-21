"""Pet_Sail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from ckeditor_uploader import urls as ck_url
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from accounts import views as account_views
from merchant_dash import views as merch_views
from contact_us_app import views as contact_views
from checkout import views as checkout_views

urlpatterns = [
    # General setup
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^contact-us/$', contact_views.new_contact, name='contact_us'),
    url(r'^about-us/$', home_views.get_about, name='about'),

    # Account URLs
    url(r'^register/$', account_views.register, name='register'),
    url(r'^profile/$', account_views.profile, name='profile'),
    url(r'^login/$', account_views.login, name='login'),
    url(r'^merchant-profile/$', account_views.merchantprofile, name='merchant'),
    url(r'^logout/$', account_views.logout, name='logout'),

    # Merchant Dashboard
    url(r'^post/(?P<id>\d+)/$', merch_views.ad_detail, name='view_ad_post'),
    url(r'^post/$', merch_views.new_ad, name='new_post'),
    url(r'^all-ads/$', merch_views.all_ads, name='adlisting'),

    # Image Upload
    url(r'^ckeditor/', include(ck_url)),

    # Holiday Sale Checkout
    url(r'^check-out/', checkout_views.checkoutview),
]
