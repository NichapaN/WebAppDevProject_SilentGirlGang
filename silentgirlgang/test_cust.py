from django.db import models
from django.conf import settings

# Create your models here.
class Customers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)
    membership_number = models.CharField(max_length=256, null=True)
    
    # first_name = models.CharField(max_length=256, null=True)
    # last_name = models.CharField(max_length=256, null=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()