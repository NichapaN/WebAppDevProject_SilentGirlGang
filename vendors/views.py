from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from tpopstore.models import Artist, Category, Product
from userprofile.models import User

from .forms import ArtistForm, ProductForm

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

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            return redirect('vendors:productlist')
    else:
        form = ProductForm()

    return render(request, 'vendors/add_product.html', {
        'form': form,
        'title': 'Add product',
        'button': 'Add product'
    })

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect('vendors:productlist')
    else:
        form = ProductForm(instance=product)

    return render(request, 'vendors/add_product.html', {
        'form': form,
        'title': 'Edit product',
        'button': 'Save changes'
    })


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'vendors/artists.html', {
        'artists': artists # to be edited to
    })

def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)

        if form.is_valid():
            artist_name = request.POST.get('artist_name')
            slug = slugify(artist_name)

            artist = form.save(commit=False)
            artist.slug = slugify(artist_name)
            artist.save()

            return redirect('vendors:artists')
    else:
        form = ArtistForm()

    return render(request, 'vendors/add_artist.html', {
        'form': form,
        'title': 'Add Artist',
        'button': 'Add new artist'
    })

def account(request):
    return render(request, 'vendors/account.html')
