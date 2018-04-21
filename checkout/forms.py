from django import forms
from accounts.models import User


class CheckoutForm(forms.ModelForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2015, 2036)]

    email = forms.CharField()
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ['email', 'stripe_id']
        exclude = ['username']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            message = "Please enter your email address"
            raise forms.ValidationError(message)

        return email
