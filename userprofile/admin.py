from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Agency

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['user', 'logo']

