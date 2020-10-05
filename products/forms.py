from django import forms
from .models import Product
from crispy_forms.helper import FormHelper

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    image_2 = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Product
        fields = ["product_name", "color", "has_size",
        "price","image", "image_2", "number_in_stock"]
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for fieldname in ["product_name", "color", "has_size",
        "price","image", "image_2", "number_in_stock"]:
            self.fields[fieldname].helper = FormHelper()
