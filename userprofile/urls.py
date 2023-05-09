from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import UserLoginForm

app_name = 'userprofile'

urlpatterns = [
    path('customersignup/', views.customersignup, name='customersignup'),
    path('agencysignup/', views.agencysignup, name='agencysignup'),
    path('customerlogin/', auth_views.LoginView.as_view(template_name='account/customerlogin.html',
                                                form_class=UserLoginForm), name='customerlogin'),
]
    