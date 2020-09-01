from django.db import models


class Country_stats(models.Model):
    country = models.CharField(max_length=254, null=True, blank=True)
    updatedAt = models.DateTimeField(name=None, auto_now=False, null=True)
    confirmed = models.CharField(max_length=254, null=True, blank=True)
    deaths = models.CharField(max_length=254, null=True, blank=True)
    recovered = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.country

    # @classmethod
    # def create(cls, country, updatedAt, confirmed, deaths, recovered):
    #     country = cls(country=country),
    #     updatedAt = cls(updatedAt=updatedAt),
    #     confirmed = cls(confirmed=confirmed),
    #     deaths = cls(deaths=deaths),
    #     recovered = cls(recovered=recovered)
    #     return country, updatedAt, confirmed, deaths, recovered
