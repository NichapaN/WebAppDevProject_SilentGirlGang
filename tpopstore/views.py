from django.shortcuts import get_object_or_404, render

from .models import *



def product_all(request):
    products = Product.products.all()
    return render(request, 'tpopstore/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'tpopstore/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'tpopstore/products/single.html', {'product': product})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tpopstore/artists.html', {
        'artists': artists
    })

def products_by_artist(request, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug)
    products = Product.objects.filter(artist=artist)
    return render(request, 'tpopstore/products/searchbyartist.html', {
        'artist': artist,
        'products': products
    })