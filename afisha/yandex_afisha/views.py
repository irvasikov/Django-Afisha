from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views import View


from .models import Places


def start_page(request):
    """Отображение стартовой страницы"""
    places_data = Places.objects.all()
    array_data_places = []
    for i in places_data:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [i.lng, i.lat]
            },
            "properties": {
                "title": i.title,
                "placeId": i.place_id,
                "detailsUrl": f"./static/places/{i.place_id}.json"
            }
        }
        array_data_places.append(feature)
    data = {
        "type": "FeatureCollection",
        "features": array_data_places
    }
    return render(request, 'start_page.html', context={"data": data})


def only_one_place_information(request, pk):
    """Отображение на отдельной странице информации о каждой отдельно локации"""
    place = serializers.serialize("json", Places.objects.filter(id=pk))
    return HttpResponse(place, content_type='application/json')