from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

class Product(models.Model):
    product_name = models.CharField(max_length=settings.CONST_PROFILE_ATTR)
    color = models.CharField(max_length=settings.CONST_PROFILE_ATTR)
    has_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = ResizedImageField(size=[400, 500], crop=['top', 'left'],quality=100, upload_to='', default='media/noimage.png')
    image_2 = ResizedImageField(size=[400, 500], crop=['top', 'left'],quality=100, upload_to='', default='media/noimage.png')
    number_in_stock = models.IntegerField(null=True , editable=True, default=0)
    is_active = models.BooleanField(default=True, null=True)
    created_by = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    created_date = models.TimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.color
    
