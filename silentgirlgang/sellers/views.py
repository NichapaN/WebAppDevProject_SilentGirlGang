from django.shortcuts import render

import tpopstore.models as storemodels

# Create your views here.

def display_product_list(request):
    product_list = storemodels.Product.objects.all()


