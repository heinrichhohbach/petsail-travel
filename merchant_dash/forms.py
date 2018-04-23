from django import forms
from django.forms import SelectDateWidget
from .models import Ad


class AdPostForm(forms.ModelForm):
    subject = forms.CharField(label='Ad Title')
    start_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    end_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    ad_price = forms.DecimalField(label="Price: (in GBP)")

    class Meta:
        model = Ad
        fields = ['subject', 'ad_summary', 'description', 'start_date', 'end_date', 'ad_price']
