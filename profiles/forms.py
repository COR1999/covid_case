from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from .models import Customer
from django_countries.fields import CountryField
from django.conf import settings
from crispy_forms.helper import FormHelper

class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=settings.CONST_PROFILE_ATTR)

    class Meta:
        model = User
        fields = (
            'first_name',
            "last_name",
            'email',
            'password1',
            'password2', )
    
    def save(self, commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.username = self.cleaned_data["email"]
        
        if commit:
            user.save()
        
        return user
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in [ "first_name","email","last_name", 'password1', 'password2']:
            self.fields[fieldname].help_text = None




class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    last_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    phone = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=True)
    city = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=False)
    address_line_2 = forms.CharField(max_length=settings.CONST_PROFILE_ADDRESS, required=False)
    class Meta:
        model = Customer
        fields = ("first_name",
        "last_name",
        "phone",
        "address_line_1",
        "address_line_2",
        "country",
        "city")
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for fieldname in ["first_name", "last_name", "phone", 
        "address_line_1", "address_line_2", "country", "city"]:
            self.fields[fieldname].helper = FormHelper()

