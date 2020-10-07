from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from .models import Customer
from django_countries.fields import CountryField
from django.conf import settings


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    # last_name = forms.CharField(max_length=settings.CONST_PROFILE_ATTR)
    email = forms.EmailField(max_length=settings.CONST_PROFILE_ATTR)
    # address_line_1 = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=True)
    # address_line_2 = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=False)
    # phone = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=True)
    # city = forms.CharField(max_length=settings.CONST_PROFILE_ATTR, required=False)
    # country = CountryField(null=True).formfield()

    class Meta:
        model = User
        fields = (
            "username",
            'first_name',
            "last_name",
            'email',
            'password1',
            'password2', )
        # fields = (
        #     "username",
        #     'first_name',
        #     "last_name",
        #     "phone",
        #     "address_line_1",
        #     "address_line_2",
        #     "country",
        #     "city",
        #     'email',
        #     'password1',
        #     'password2', )
    
    def save(self, commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        
        if commit:
            user.save()
        
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', "first_name","last_name", 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            # self.fields[fieldname].widget.attrs['placeholder'] = ''




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
        "phone", "email",
        "country",
        "address_line_1",
        "address_line_2",
        "city")
    
