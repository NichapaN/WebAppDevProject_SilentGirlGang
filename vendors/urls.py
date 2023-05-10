from django.urls import path

from . import views

app_name = 'vendors'

urlpatterns = [
    path('productlist/', views.product_listing, name="productlist"),
    path('add-product/', views.add_product, name="add_product"),
    path('add-artist/', views.add_artist, name="add_artist"),
    path('account', views.account, name="account"),
    path('artists/', views.artists, name="artists"),
    path('<slug:vendors_product>/', views.edit_product_details, name="editproductdetails"),
    path('edit-product/<int:pk>/', views.edit_product, name="edit_product"),
]