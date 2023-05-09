from django.contrib import admin
import buyers.models as buyers_models
from . import models

# Register your models here.

@admin.register(buyers_models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10    
    list_display = ['first_name','last_name','membership','gender']
    list_editable = ['membership','gender']
    ordering = ['first_name','last_name']
    search_fields = ['first_name__startswith','last_name__startswith']
    #@admin.display(models.Customer)