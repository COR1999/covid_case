from django.db import models
from django_countries.fields import CountryField
from django.conf import settings

class Product(models.Model):
    product_name = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    has_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    number_in_stock = models.IntegerField(null=True , editable=True, default=0)
    def __str__(self):
        return self.color



class Order(models.Model):
    firstname = models.CharField(max_length=254, null=True)
    lastname = models.CharField(max_length=254, null=True)
    email = models.CharField(max_length=254, null=True)
    address_1 = models.CharField(max_length=1000, editable=True, null=True)
    address_2 = models.CharField(max_length=1000, default="", editable=True, null=True)
    city = models.CharField(max_length=1000, null=True)
    country = CountryField(null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + self.lastname


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return self.item
