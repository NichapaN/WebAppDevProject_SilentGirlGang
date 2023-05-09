from django.urls import path

from . import views

app_name = 'tpopstore'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('artists/', views.artist_list, name='artists_list'),
    path('shopbyartist/<slug:artist_slug>/', views.products_by_artist, name='products_by_artist'),
]