from django.shortcuts import render, get_object_or_404

from tpopstore.models import Artist, Category, Product

# Create your views here.
def product_listing(request):
    category = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'vendors/product_listing.html', {
        'category': category,
        'products': products
    })

def edit_product_details(request, vendors_product):
    product = get_object_or_404(Product, slug=vendors_product)
    return render(request, 'vendors/edit_product_details.html', {
        'product': product
    })

def artists(request):
    artists = Artist.objects.all()
    return render(request, 'vendors/artists.html', {
        'artists': artists # to be edited to
    })

def account(request):
    return render(request, 'vendors/account.html')
