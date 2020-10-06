from django.db import models
from django.utils import tree
from profiles.models import Customer
from django_countries.fields import CountryField
from products.models import Product
from django.conf import settings





class Order(models.Model):
    user_profile = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    stripe_pid = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=False, blank=False, default='')
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    order_confirmed = models.BooleanField(default=False)

    

class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True , editable=True, default=0)
    def __str__(self):
        return self.item.color

