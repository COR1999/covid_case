from django.db import models
from profiles.models import Customer
from django_countries.fields import CountryField
from products.models import Product
from django.conf import settings

class Order(models.Model):
    user_profile = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    stripe_pid = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=False, blank=False, default='')
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # referance from customer model
    
    firstname = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    lastname = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    email = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    address_1 = models.CharField(max_length=settings.CONST_PROFILE_ADDRESS, editable=True, null=True)
    address_2 = models.CharField(max_length=settings.CONST_PROFILE_ADDRESS, default="", editable=True, null=True)
    city = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    country = CountryField(null=True)
    

    def __str__(self):
        return self.firstname + self.lastname

class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True , editable=True, default=0)
    def __str__(self):
        return self.item