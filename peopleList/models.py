from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    education = models.CharField(max_length=64)
    degree = models.CharField(max_length=64)
    email = models.EmailField(max_length=225)
    address = models.CharField(max_length=64)
    postalCode = models.CharField(max_length=64)

