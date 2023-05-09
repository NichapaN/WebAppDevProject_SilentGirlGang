from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)
    
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('tpopstore:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Artist(models.Model):
    artist_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.artist_name

    class Meta:
        ordering = ['artist_name']

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    artist = models.ForeignKey(Artist, related_name="product", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_inventory_status(self):
        if self.in_stock == True:
            status = 'In stock'
        else:
            status = 'Out of stock'
        return status

    def get_absolute_url(self):
        return reverse('tpopstore:product_detail', args=[self.slug])
    
    def get_product_url_for_vendor(self):
        return reverse('vendors:editproductdetails', args=[self.slug])

    def __str__(self):
        return self.title