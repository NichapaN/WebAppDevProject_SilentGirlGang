from django.contrib import admin

import sellers.models as sellers_models
import buyers.models as buyers_models
# Register your models here.

@admin.register(sellers_models.Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = [
        "agency_name",
        "phone",
        "email",
    ]
    
    search_fields = ['agency_name']
    
@admin.register(sellers_models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_per_page=10
    search_fields = ['artist_name']
    
@admin.register(sellers_models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_per_page=10
    search_fields = ['title']
    
@admin.register(sellers_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = [
        "title",
        "description",
        "price",
        "inventory",
        "inventory_status",
        "inventory_value",
        "last_update",
        "collection",
        "category"
    ]
    search_fields = ['title']
    
    def inventory_value(self,product):
        return product.inventory * product.price
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return "Low"
        else:
            return "OK"
    

@admin.register(buyers_models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10    
    list_display = ['first_name','last_name','membership','gender']
    list_editable = ['membership','gender']
    ordering = ['first_name','last_name']
    search_fields = ['first_name__startswith','last_name__startswith']
    #@admin.display(models.Customer)
   

@admin.register(buyers_models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display= ['customer','street','city']
    
    
@admin.register(buyers_models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_per_page= 10
      
@admin.register(buyers_models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_per_page= 10

@admin.register(buyers_models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page= 10
    list_display=['placed_at','customer','payment_status']
    list_editable = ['payment_status']
    
@admin.register(buyers_models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_per_page= 10

