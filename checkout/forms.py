from django import forms
from checkout.models import Checkout



class CheckoutForm(forms.ModelForm):
    Choices = (('Payments', 'Check Payments'), ('Delivery', 'Cash on Delivery'), ('Paypal', 'Paypal'))
    payment = forms.ChoiceField(required=True, choices=Choices, widget=forms.RadioSelect)
    class Meta:
        model = Checkout
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'country',
            'adress',
            'city',
            'state',
            'postal_code',
            'create_an_account',
            'free_shipping',
            'local_pickup',
            'payment'
        )
