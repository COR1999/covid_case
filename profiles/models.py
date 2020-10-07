from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    first_name = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    last_name = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    phone = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    email = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    city = models.CharField(max_length=settings.CONST_PROFILE_ATTR, null=True)
    address_line_1 = models.CharField(max_length=settings.CONST_PROFILE_ADDRESS, null=True)
    address_line_2 = models.CharField(max_length=settings.CONST_PROFILE_ADDRESS, null=True, default="")
    country = CountryField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)





