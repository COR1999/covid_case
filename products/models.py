from django.db import models


class Product(models.Model):

    product_name = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    has_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
