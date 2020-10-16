from django.shortcuts import render, redirect, reverse
from .models import Product
from django.conf import settings
import requests
import json
from .forms import ProductForm
from django.contrib import messages
# Enabled this to get the screenshot for the readme using http://ami.responsivedesign.is/
# from django.views.decorators.clickjacking import xframe_options_exempt
# @xframe_options_exempt

def all_products(request):
    """
        A view that calls the api and if the status code is 200 
        pass the information from the api call to the template.
    """
    response = requests.get(
        settings.BASE_URL + settings.COUNTRY_DATA_WORLDMETERS)

    country_data = []
    if response.status_code == 200:
        all_data = json.loads(response.content.decode("utf-8"))
        try:
            for country in all_data:               
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
                    country_data.append(country_data_set)
        except Exception as e:
            # If there is any problem proccessing the response data - inform the user.
            print("Exception:", e)
            messages.error(request, "Sorry failed loading map data")
    else:
        # Problem with Disease.sh - inform user.
        messages.error(request, "There has been a problem getting map data. Please try again later.")
        
    products = Product.objects.filter(is_deleted=False).order_by("-number_in_stock")
    context = {
        "products": products,
        "country_data": country_data
    }
    return render(request, "products/all_products.html", context)


def create_product(request):
    """A view the creates a product"""
    form = ProductForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("products"))

    context = {
        "form": form,
    }

    return render(request, "products/products_form.html", context)



def update_product(request, id):
    """This view gets a product from the database by using the id then updateing it if the form is valid"""
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse("products"))
    else:
        form = ProductForm(request.POST or None, instance=product)
    
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/products_form.html", context)


def delete_product(request, id):
    """A view that set the is_deleted attribute to True"""
    if request.method == "POST":
        product = Product.objects.get(id=id)
        # Checking to see if the get returns the product incase product has allready been deleted from database.
        if product:
            product.is_deleted = True
            product.save()
            
    return redirect(reverse("products"))
        