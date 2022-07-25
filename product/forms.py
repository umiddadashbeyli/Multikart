from django import forms
from product.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {
            'title',
            'body'
        }
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'review',
                'placeholder' : 'Enter your Review Subjects'
            }),
            'body' : forms.Textarea(attrs={
                'class' : 'form-control',
                'id' : 'exampleFormControlTextarea1',
                'placeholder' : 'Enter your Review Subjects',
                'rows' : 6
            })
        }