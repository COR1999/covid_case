from django import forms
from .models import Product, Supplier
from crispy_forms.helper import FormHelper

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    image_2 = forms.ImageField(required=False, widget=forms.FileInput)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), label='Supplier', widget=forms.Select)
    use_required_attribute = False
    class Meta:
        model = Product
        fields = ["product_name", "color",
        "price","image", "image_2", "number_in_stock", "supplier"]
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for fieldname in ["product_name", "color",
        "price","image", "image_2", "number_in_stock", "supplier"]:
            self.fields[fieldname].helper = FormHelper()
