from django.db import models

from django.contrib.auth.models import AbstractUser,  PermissionsMixin, BaseUserManager

# Create your models here.


class CustomAccountManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')
        if not password:
            raise ValueError('You must provide password')

        
        user = self.model(email=self.normalize_email(email),
                          **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, first_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', True)
        return self._create_user( email, password, first_name, **other_fields)

    def create_superuser(self, email, password, first_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self._create_user( email, password, first_name, **other_fields)

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"
    #pass
