from django import forms
from profiles.models import Customer
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings

class OrderForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    last_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    email = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    address_line_1 = forms.CharField(max_length=settings.CONST_PROFILE_ADDRESS)
    address_line_2 = forms.CharField(max_length=settings.CONST_PROFILE_ADDRESS, required=False)
    city = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    country = CountryField(null=True).formfield()
    
    class Meta:
        model = Customer
        fields = ["first_name", "last_name",
                    "email", "address_line_1",
                    "address_line_2", "city", "country"]
