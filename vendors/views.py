from django.shortcuts import render, get_object_or_404

from tpopstore.models import Category, Product

# Create your views here.
def product_listing(request):
    category = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'vendors/product_listing.html', {
        'category': category,
        'products': products
    })

def edit_product_details(request):
    return render(request, 'vendors/edit_product_details.html')

def artists(request):
    products = Product.objects.all()
    return render(request, 'vendors/artists.html', {
        'products': products # to be edited to artists
    })

def account(request):
    return render(request, 'vendors/account.html')
