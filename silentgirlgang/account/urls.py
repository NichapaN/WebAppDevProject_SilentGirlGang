from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
#from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('customersignup/', views.customersignup, name='customersignup'),
    path('agencysignup/', views.agencysignup, name='agencysignup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
]
    
