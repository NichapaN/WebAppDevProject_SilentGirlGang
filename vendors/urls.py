from django.urls import path

from . import views

app_name = 'vendors'

urlpatterns = [
    path('productlist/', views.product_listing, name="productlist"),
    path('account', views.account, name="account"),
    path('artists/', views.artists, name="artists"),
    path('<slug:vendors_product>/', views.edit_product_details, name="editproductdetails"),
]