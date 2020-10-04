from django import forms
from profiles.models import Customer
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings

class OrderForm(forms.Form):
    
    firstname = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    lastname = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    user_email = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    address_1 = forms.CharField(max_length=settings.CONST_PROFILE_ADDRESS)
    address_2 = forms.CharField(max_length=settings.CONST_PROFILE_ADDRESS, required=False)
    city = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    country = CountryField(null=True).formfield()
    
    class Meta:
        model = User
        fields = ["firstname", "lastname",
                    "user_email", "address_1",
                    "address_2", "city", "country"]