from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Agency)
admin.site.register(Artist)
admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
