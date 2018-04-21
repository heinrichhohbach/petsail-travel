from django import forms
from contact_us_app.models import ContactUs


class ContactUsForm(forms.ModelForm):
    QUERY_CHOICES = (
        ('Merchant Problems', 'Merchant Problems'),
        ('Buyer Problems', 'Buyer Problems'),
        ('Billing Problems', 'Billing Problems'),
        ('General Chat', 'General Chat')
    )

    contact_title = forms.CharField(
        label='Subject'
    )

    contact_name = forms.CharField(
        label='Name'
    )

    query_type = forms.ChoiceField(
        label='What is your query related to?',
        choices=QUERY_CHOICES
    )

    class Meta:
        model = ContactUs
        fields = ['contact_title', 'contact_name', 'contact_email', 'query_type',
                  'query_text']

    def clean_email(self):
        email = self.cleaned_data.get('contact_email')

        if not email:
            message = "Please enter your email address"
            raise forms.ValidationError(message)

        return email
