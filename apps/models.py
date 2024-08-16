from django.db import models

# Create your models here.
class Product(models.Model):
    nama = models.CharField(max_length=21)