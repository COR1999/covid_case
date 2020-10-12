from django.db import models
from profiles.models import Customer
from products.models import Product
from django.conf import settings





class Order(models.Model):
    customer_profile = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    stripe_pid = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=False, blank=False, default='')
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    order_confirmed = models.BooleanField(default=False)
    date_dispatched = models.DateTimeField(null=True)
    

class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True , editable=True, default=0)
    def line_total(self):
        return self.quantity * self.item.price

