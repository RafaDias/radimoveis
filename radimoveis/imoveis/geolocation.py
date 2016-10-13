import googlemaps
from django.conf import settings


def location_a_partir_do(endereco):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    geocode_result = gmaps.geocode(endereco)
    if not geocode_result:
        return

    return geocode_result[0]['geometry']['location']
