from django import forms
from django_countries.fields import CountryField


class OrderForm(forms.Form):
    # class Meta:
    #     model = products.models.Order
    #     fields = ("")
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label="E-Mail")
    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField()
    country = CountryField()