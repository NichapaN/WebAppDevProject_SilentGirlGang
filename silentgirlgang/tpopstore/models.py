from django.db import models

# Create your models here.

# Agency -> Artist -> Product
# Customer , Cart, Order

class Agency(models.Model):
    agency_name = models.CharField(max_length=255)

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
