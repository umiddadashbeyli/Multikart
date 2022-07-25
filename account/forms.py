import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  password_validation
from django.utils.translation import gettext_lazy as _
from account.models import User



class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'id' : 'uname',
            'placeholder' : 'Username'
        }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
            'class' : 'form-control', 
            'id' : 'fname', 
            'placeholder' : 'First Name'
        }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
            'class' : 'form-control', 
            'id' : 'lname', 
            'placeholder' : 'Last Name'
        }))
    bio = forms.Textarea(attrs={
            'class' : 'form-control', 
            'id' : 'bio', 
            'placeholder' : 'Bio'
        })
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
            'class' : 'form-control', 
            'id' : 'email', 
            'placeholder' : 'Email'
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'username', 'bio', 'image']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user






class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'id' : 'email',
        'placeholder' : 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'id' : 'review',
        'placeholder' : 'Enter your password'
    }))


class ChangePasswordForm(forms.Form):
  
    oldpassword = forms.CharField(
        label='Old password',
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
    }))
    newpassword1 = forms.CharField(
        label='New password',
        strip=False,
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          }),
        
    )
    newpassword2 = forms.CharField(
        label='Mew password',
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean(self):
        newpassword1 = self.cleaned_data.get('newpassword1')
        newpassword2 = self.cleaned_data.get('newpassword2')
        if newpassword1 != newpassword2:
            raise forms.ValidationError('password and confirm password is not same')
        return super().clean()


