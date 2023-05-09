from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#User = get_user_model()
from .models import User
from django.contrib.auth.forms import UserCreationForm
from buyers.models import Customer



class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=10, required=True)
    

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'phone', 'password1', 'password2',]

class AgencySignUpForm(UserCreationForm):
    agency_name = forms.EmailField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=10, required=True)
    image = forms.ImageField(upload_to=, blank=True, null=True)

    class Meta:
        model = User
        fields = ['username', 'agency_name', 'email', 'phone', 'image', 'password1', 'password2',]