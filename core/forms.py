from django import forms
from core.models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'name' : 'EMAIL',
                'id' : 'mce-EMAIL',
                'placeholder' : 'Enter your email',
                'required' : 'required',
            })
        }