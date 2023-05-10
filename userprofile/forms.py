from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#User = get_user_model()
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models




class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=10, required=True)
    

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'phone', 'password1', 'password2',]

class AgencySignUpForm(UserCreationForm):
    agency_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=10, required=True)
    #image = forms.ImageField(upload_to='userprofile/')
    address = forms.CharField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ['username', 'agency_name', 'email', 'phone', 'address', 'password1', 'password2',]


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

class AgencyLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))