from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# Agency -> Artist -> Product
# Customer , Cart, Order

# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
#     one_click_purchasing = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

class Agency(models.Model):
    agency_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    # logo

    def __str__(self):
        return self.agency_name

    class Meta:
        ordering = ['agency_name']

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.artist_name

    class Meta:
        ordering = ['artist_name']

class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Product(models.Model):

    CATEGORY_ALBUM = 'A'
    CATEGORY_MERCHANDISE = 'M'

    CATEGORY_CHOICES = [
        (CATEGORY_ALBUM, 'Album'),
        (CATEGORY_MERCHANDISE, 'Merchandise'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, 
    null=True)
    category = models.CharField(max_length=1,
        choices=CATEGORY_CHOICES, 
        default=CATEGORY_ALBUM)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    #MEMBERSHIP_JADE = 'J'
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'GOLD'),
    ]

    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Others'),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10,
        choices=GENDER_CHOICES, 
        default=GENDER_FEMALE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,
        choices=MEMBERSHIP_CHOICES, 
        default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    # def __str__(self):
        # return str(self.id)
        # return self.transaction_id

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    address = models.CharField(max_length=255, default="123/456")
    street = models.CharField(max_length=255, default="Silom")
    city = models.CharField(max_length=255, default="Bangkok")
    zipcode = models.CharField(max_length=255, default="000000")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    # default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.address} {self.street}, {self.city}"