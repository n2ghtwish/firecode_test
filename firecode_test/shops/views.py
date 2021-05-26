from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


# Create your views here.
class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({'cities': serializer.data})


class StreetView(APIView):
    def get(self, request):
        if 'city_id' in request.query_params.keys():
            city = City.objects.get(pk=int(request.query_params['city_id']))
            streets = Street.objects.filter(city=city)
        else:
            streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response({'streets': serializer.data})


class ShopView(APIView):
    def get(self, request):
        shops = Shop.objects.all()
        if len(request.query_params) > 0:
            if 'city' in request.query_params.keys():
                city = City.objects.get(pk=int(request.query_params['city']))
                shops = shops.filter(city=city)
            if 'street' in request.query_params.keys():
                street = Street.objects.get(pk=int(request.query_params['street']))
                shops = shops.filter(street=street)
        serializer = ShopSerializer(shops, many=True)
        return Response({'shops': serializer.data})
