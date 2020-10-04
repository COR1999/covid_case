from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from .models import Customer
from django_countries.fields import CountryField
from django.conf import settings


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=100, help_text='Last Name')
    # last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=settings.CONST_PROFILE_ATTR)
    address_line_1 = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=True)
    address_line_2 = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=False)
    phone = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=False)
    city = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=False)
    country = CountryField(null=True).formfield()
    class Meta:
        model = User
        fields = ("username",
        'first_name',
        "last_name", "phone",
        "address_line_1",
        "address_line_2",
        "country",
        "city",'email',
        'password1', 'password2', )

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    last_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    address_line_2 = CharField(max_length=settings.CONST_PROFILE_ADDRESS,default="")
    class Meta:
        model = Customer
        fields = ["first_name",
        "last_name",
        "phone", "email",
        "country",
        "address_line_1",
        "address_line_2",
        "city"]
    
