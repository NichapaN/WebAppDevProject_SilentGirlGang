from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import UserLoginForm, AgencyLoginForm

app_name = 'userprofile'

urlpatterns = [
    path('customersignup/', views.customersignup, name='customersignup'),
    path('agencysignup/', views.agencysignup, name='agencysignup'),
    path('customerlogin/', auth_views.LoginView.as_view(template_name='account/customerlogin.html',
                                                form_class=UserLoginForm), name='customerlogin'),
    path('agencylogin/', auth_views.LoginView.as_view(next_page='vendors:productlist',template_name='account/agencylogin.html',
                                                form_class=AgencyLoginForm), name='agencylogin'),
    path('logout/', auth_views.LogoutView.as_view(next_page='tpopstore:product_all'), name='logout'),
]
    