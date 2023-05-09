from django.urls import path

from . import views

app_name = 'vendors'

urlpatterns = [
    path('productlist/', views.product_listing, name="productlist"),
    path('editproductdetails/', views.edit_product_details, name="editproductdetails"),
    path('artists/', views.artists, name="artists"),
    path('account', views.account, name="account"),
]