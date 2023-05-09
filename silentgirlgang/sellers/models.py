from django.db import models
from django.conf import settings
# Create your models here.


class Agency(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    # logo

    def __str__(self):
        return self.user.agency_name

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

#comeback1,2,3


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
    
