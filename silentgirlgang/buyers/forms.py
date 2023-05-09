from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User

from .models import Customer


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=['first_name', 'last_name', 'email', 'phone']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
        }
