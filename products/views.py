from django.shortcuts import render
from .models import Product
from django.conf import settings


def all_products(request):

    products = Product.objects.all()
    print(products)
    print("media root", settings.MEDIA_URL)
    context = {
        "products": products,
    }
    return render(request, "products/all_products.html", context)
