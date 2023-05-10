from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    #pass

    def __str__(self):
        return self.username

class Agency(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   logo = models.ImageField(upload_to='images/', default='images/default.png')

   def __str__(self):
        return self.user.username
   