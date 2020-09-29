from django import forms
from profiles.models import Customer
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    address_line_1 = forms.CharField(max_length=150)
    address_line_2 = forms.CharField(max_length=150)
    country = CountryField(null=True).formfield()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "address_line_1", "address_line_2", "country"]
    
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField(label="E-Mail")
    # address_line_1 = forms.CharField()
    # address_line_2 = forms.CharField()
    # country = CountryField()
