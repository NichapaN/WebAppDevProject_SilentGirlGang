from django.db import models

# Create your models here.

# Agency -> Artist -> Product
# Customer , Cart, Order

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

    def __str__(self):
        return self.title

class Customer(models.Model):
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

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True
        )
    
    def __str__(self):
        return f"{self.street}, {self.city} "

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, 
    null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField()

