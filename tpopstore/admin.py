from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'user_id', 'artist', 'slug', 'price', 'inventory'
                    , 'inventory_status', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'inventory', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    