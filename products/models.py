from django.db import models

from django.conf import settings

class Product(models.Model):
    product_name = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    has_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='media/', default='media/noimage.png')
    image_2 = models.ImageField(upload_to='media/', default='media/noimage.png')
    number_in_stock = models.IntegerField(null=True , editable=True, default=0)
    is_active = models.BooleanField(default=True, null=True)
    created_by = models.CharField(max_length=254, null=True)
    created_date = models.TimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.color


