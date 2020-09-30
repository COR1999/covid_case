from django.shortcuts import render, redirect, reverse
from .models import Product
from django.conf import settings
import requests
import urllib3
import json
from .forms import ProductForm


def all_products(request):
    response = requests.get(
        settings.BASE_URL + settings.COUNTRY_DATA_WORLDMETERS)

    if response.status_code == 200:
        all_data = json.loads(response.content.decode("utf-8"))
        country_data = []
        for country in all_data:
            try:
                country_name = country["country"]
                country_code = country["countryInfo"]["iso2"]
                country_cases = country["cases"]
                country_todayCases = country["todayCases"]
                country_deaths = country["deaths"]
                country_recovered = country["recovered"]
                casesPerOneMillion = country["casesPerOneMillion"]
                deathsPerOneMillion = country["deathsPerOneMillion"]
                country_population = country["population"]
                country_data_set = {
                    "country": country_name,
                    "code": country_code,
                    "cases": country_cases,
                    "todayCases": country_todayCases,
                    "deaths": country_deaths,
                    "recovered": country_recovered,
                    "population": country_population,
                    "casesPerOneMillion": casesPerOneMillion,
                    "deathsPerOneMillion": deathsPerOneMillion,
                }
                # print(country_population)
                country_data.append(country_data_set)

            except Exception as e:
                print("Exception:", e)

    products = Product.objects.all()

    # grand_total = request.session.get("grand_total", {})
    # quantity = request.session.get('quantity', 0)

    context = {
        "products": products,
        # "grand_total": grand_total,
        "country_data": country_data
    }
    return render(request, "products/all_products.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse("products"))

    context = {
        "form": form,
    }

    return render(request, "products/products_form.html", context)



def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None,instance=product)

    if form.is_valid():
        form.save()
        return redirect(reverse("products"))
    
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/products_form.html", context)


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.delete()
        return redirect(reverse("products"))

    context = {
        "product": product,
    }
    return render(request, "products/product_delete_confirm.html", context)