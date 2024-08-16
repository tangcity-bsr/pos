from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from datetime import datetime
# import timezone

class UsersManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        # Buat user baru dengan menggunakan phone_number sebagai identitas unik
        if not username:
            raise ValueError('The username field must be set')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        # Buat superuser dengan menggunakan phone_number sebagai identitas unik
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

# Create your models here.
class Users(AbstractUser):
    ROLE_CHOICES = (
        ('root', 'Root'),
        ('admin', 'Admin'),
        ('supervisor', 'Supervisor'),
        ('employee', 'Staf'),
        ('auditor', 'Auditor'),
    )
    id = models.AutoField(primary_key=True)
    username = models.CharField(null=False, blank=False, unique=True, max_length=21)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    number_phone = models.CharField(max_length=14, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    objects = UsersManager()

    def __str__(self):
        return self.username