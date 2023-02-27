from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)

    def __str__(self):
        return self.country


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
