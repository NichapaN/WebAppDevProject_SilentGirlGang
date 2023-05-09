from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerSignUpForm, AgencySignUpForm
# Create your views here.

@login_required
def myaccount(request):
    return render(request, 'account/myaccount.html')

def customersignup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = CustomerSignUpForm()

    return render(request, 'account/customersignup.html', {'form': form})
            

def agencysignup(request):
    if request.method == 'POST':
        form = AgencySignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = AgencySignUpForm()

    return render(request, 'account/agencysignup.html', {'form': form})
            