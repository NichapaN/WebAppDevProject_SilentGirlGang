from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
#from .forms import UserLoginForm

app_name = 'userprofile'

urlpatterns = [
    path('customersignup/', views.customersignup, name='customersignup'),
    path('agencysignup/', views.agencysignup, name='agencysignup'),
]
    