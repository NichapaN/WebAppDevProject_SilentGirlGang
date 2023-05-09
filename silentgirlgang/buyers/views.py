from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from . models import Customer
from . forms import CustomerProfileForm


# Create your views here.

class Profileview(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'buyer/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name' ]
            last_name = form.cleaned_data['last_name' ]
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            user=user
            reg = Customer(first_name=first_name, last_name=last_name, email=email,
            phone=phone, user=user)
            reg.save()
            messages.success(request,"Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'buyer/profile.html',locals())