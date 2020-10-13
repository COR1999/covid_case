from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=settings.CONST_PROFILE_ATTR)
    description = models.CharField(max_length=settings.CONST_PROFILE_ATTR)
    def __str__(self):
        return self.supplier_name

class Product(models.Model):
    product_name = models.CharField(max_length=settings.CONST_PROFILE_ATTR)
    color = models.CharField(max_length=settings.CONST_PROFILE_ATTR)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = ResizedImageField(size=[400, 500], crop=['middle', 'center'],quality=100, upload_to='', default='noimage.jpg')
    image_2 = ResizedImageField(size=[400, 500], crop=['middle', 'center'],quality=100, upload_to='', default='noimage.jpg', null=True)
    number_in_stock = models.IntegerField(null=True , editable=True, default=0)
    is_active = models.BooleanField(default=True, null=True)
    created_by = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    created_date = models.TimeField(auto_now_add=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.color
    



