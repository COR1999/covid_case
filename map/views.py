from django.shortcuts import render
from django.conf import settings
import requests
import urllib3
import json
from .models import Country_stats
from django.core import serializers
import pycountry


def load_map(request):
    response = requests.get(settings.BASE_URL + settings.COUNTRY_DATA_JHUCSSE)
    index = 0
    if response.status_code == 200:
        all_data = json.loads(response.content.decode("utf-8"))
        # country_code = ""
        # for country in all_data:
        while index < 3:
            country = all_data[index]
            try:
                map_country_names(country)
                country_code = country["country_code"]
                print("in try", country_code)
                # if Country_stats.objects.find
                # change create to update ?
                # Country_stats.objects.create(country=country["country"],
                #                              #  country_code=country["country_code"],
                #                              country_code=country_code,
                #                              updatedAt=country["updatedAt"],
                #                              confirmed=country["stats"]["confirmed"],
                #                              deaths=country["stats"]["deaths"],
                #                              recovered=country["stats"]["recovered"])
            except LookupError as e:
                print("yo", e)
            index += 1

    country_data = Country_stats.objects.all()[:3]
    print("country_Data", country_data[0].country_code)
    final_data = serializers.serialize('json', country_data)
    # print("final_data", final_data)
    context = {
        "country_data": final_data,
    }
    return render(request, "map/map.html", context)


def map_country_names(country):
    country["country_code"] = ""

    if str(country["country"]) == "Burma":
        country["country"] = "Myanmar"
    if str(country["country"]) in "Congo (Brazzaville)":
        country["country"] = "congo"
    if str(country["country"]) in "Congo (Kinshasa)":
        country["country"] = "congo"
    if str(country["country"]) in "Korea, South":
        country["country"] = ""
    if str(country["country"]) in "Diamond Princess":
        country["country"] = ""

    country_code = pycountry.countries.search_fuzzy(str(country["country"]))
    # print(str(country["country"]))
    if len(country_code):
        country["country_code"] = country_code[0].alpha_2
        # print(country_code[0].alpha_2)
    else:
        country["country_code"] = ""
    # print("end of function", country)
    return
