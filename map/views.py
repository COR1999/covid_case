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
    if response.status_code == 200:
        all_data = json.loads(response.content.decode("utf-8"))
        country_code = ""
        for country in all_data:
            try:
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
                if str(country["country"]) == pycountry.countries.search_fuzzy(
                        str(country["country"])):
                    country["country"] = pycountry.countries.search_fuzzy(
                        str(country["country"]))
                else:
                    country["country"] = ""
            except LookupError as e:
                print(e)

            Country_stats.objects.create(country=country["country"],
                                         country_code=country_code,
                                         updatedAt=country["updatedAt"],
                                         confirmed=country["stats"]["confirmed"],
                                         deaths=country["stats"]["deaths"],
                                         recovered=country["stats"]["recovered"])

    country_data = Country_stats.objects.all()[:5]
    final_data = serializers.serialize('json', country_data)
    context = {
        "country_data": final_data,
        "MAPBOX_PUBLIC_KEY": settings.MAPBOX_PUBLIC_KEY,
    }
    return render(request, "map/map.html", context)
