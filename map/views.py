from django.shortcuts import render
from django.conf import settings
import requests
import urllib3
import json
from .models import Country_stats


def load_map(request):
    response = requests.get(settings.BASE_URL + settings.COUNTRY_DATA_JHUCSSE)
    if response.status_code == 200:
        all_data = json.loads(response.content.decode("utf-8"))
        index = 0
        country = []
        updatedAt = []
        confirmed = []
        deaths = []
        recovered = []
        for country_stats in all_data:
            Country_stats.objects.create(country=country_stats["country"],
                                         updatedAt=country_stats["updatedAt"],
                                         confirmed=country_stats["stats"]["confirmed"],
                                         deaths=country_stats["stats"]["deaths"], recovered=country_stats["stats"]["recovered"])
        print(len(all_data))
        while index < len(all_data):
            # for key in all_data[index]:
            # print(all_data[index][key])
            country.append(all_data[index]["country"])
            updatedAt.append(all_data[index]["updatedAt"])
            confirmed.append(all_data[index]["stats"]["confirmed"])
            deaths.append(all_data[index]["stats"]["deaths"])
            recovered.append(all_data[index]["stats"]["recovered"])
            index += 1
        # context = {
        #     "all_data": all_data,
        #     "country": country,
        #     "updatedAt": updatedAt,
        #     "confirmed": confirmed,
        # }
        print(Country_stats.objects.all())
        context = {
            "country_stats": Country_stats.objects.all(),
        }
        return render(request, "map/map.html", context)
    else:
        render(request, "map/map.html",)
