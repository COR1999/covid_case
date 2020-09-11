from django.shortcuts import render
from django.conf import settings
import requests
import urllib3
import json
# from .models import Country_stats


def load_map(request):
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

    # country_data = Country_stats.objects.all()[:3]
    # print("country_Data", country_data[0].country_code)
    # final_data = serializers.serialize('json', all_data)
    # print("final_data", country_data)
    context = {
        "country_data": country_data,
    }
    return render(request, "map/map.html", context)
