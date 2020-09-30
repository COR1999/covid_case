from django import forms
from profiles.models import Customer
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class OrderForm(forms.Form):
    
    firstname = forms.CharField(max_length=254)
    lastname = forms.CharField(max_length=254)
    user_email = forms.CharField(max_length=254)
    address_1 = forms.CharField(max_length=254)
    address_2 = forms.CharField(max_length=254)
    city = forms.CharField(max_length=254)
    country = CountryField(null=True).formfield()
    
    class Meta:
        model = User
        fields = ["firstname", "lastname",
                    "user_email", "address_1",
                    "address_2", "city", "country"]