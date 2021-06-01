import json
from datetime import datetime
from playhouse.shortcuts import model_to_dict
import peewee

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Street, Shop, PeeWeeCity, PeeWeeStreet, PeeWeeShop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer, AddShopSerializer


# Create your views here.
class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        # return Response({'cities': serializer.data})
        resp = Response({'cities': serializer.data})
        return resp


class PeeWeeCityView(APIView):
    def get(self, request):
        cities = list(PeeWeeCity.select(PeeWeeCity.name).dicts())
        return Response(json.dumps({'peewee_cities': cities}, ensure_ascii=False,
                                   indent=4), content_type='application/json')


class StreetView(APIView):
    def get(self, request):
        if 'city_id' in request.query_params.keys():
            city = City.objects.get(pk=int(request.query_params['city_id']))
            streets = Street.objects.filter(city=city)
        else:
            streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response({'streets': serializer.data})


class PeeWeeStreetView(APIView):
    def get(self, request):
        if 'city_id' in request.query_params.keys():
            city_id = int(request.query_params['city_id'])
            streets = list(PeeWeeStreet.select(PeeWeeStreet.name).where(PeeWeeStreet.city == city_id).dicts())
        else:
            streets = list(PeeWeeStreet.select(PeeWeeStreet.name).dicts())
        return Response(json.dumps({'peewee_cities': streets}, ensure_ascii=False,
                                   indent=4), content_type='application/json')


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
            if 'open' in request.query_params.keys():
                ct = datetime.now().time()
                if request.query_params['open'] == '0':
                    shops = shops.exclude(opens__lte=ct, closes__gte=ct)
                elif request.query_params['open'] == '1':
                    shops = shops.filter(opens__lte=ct, closes__gte=ct)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ShopSerializer(shops, many=True)
        return Response({'shops': serializer.data})

    def post(self, request):
        shop = request.data.get('shop')
        serializer = AddShopSerializer(data=shop)
        if serializer.is_valid(raise_exception=True):
            shop_saved = serializer.save()
            return Response({'id': shop_saved.pk})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PeeWeeShopView(APIView):
    def get(self, request):
        shops = PeeWeeShop.select(PeeWeeShop.name, PeeWeeCity.name, PeeWeeStreet.name).join(PeeWeeCity, attr='city').join(PeeWeeStreet, attr='street')
        # shops = PeeWeeShop.select().join(PeeWeeCity, attr='city').join(PeeWeeStreet, attr='street')
        # shops = PeeWeeShop.select(PeeWeeShop.name, PeeWeeCity.name, PeeWeeStreet.name).join(PeeWeeCity, PeeWeeStreet)
        if len(request.query_params) > 0:
            if 'city' in request.query_params.keys():
                city_id = int(request.query_params['city'])
                shops = shops.where(PeeWeeShop.city == city_id)
            if 'street' in request.query_params.keys():
                street_id = int(request.query_params['street'])
                shops = shops.where(PeeWeeShop.street == street_id)
            if 'open' in request.query_params.keys():
                ct = datetime.now().time()
                if request.query_params['open'] == '0':
                    pass
                    shops = shops.where((PeeWeeShop.opens > ct) | (PeeWeeShop.closes < ct))
                elif request.query_params['open'] == '1':
                    shops = shops.where(PeeWeeShop.opens < ct, PeeWeeShop.closes > ct)
            # else:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # serializer = ShopSerializer(shops, many=True)
        # return Response({'shops': serializer.data})
        # shops = list(shops.select(PeeWeeShop.name, PeeWeeShop.city.name, PeeWeeShop.street.name).dicts())
        for row in shops:
            print(row.name, row.city.name, row.street.name)
        # shops = list(shops.dicts())
        return Response(json.dumps({'peewee_cities': shops}, ensure_ascii=False,
                                   indent=4), content_type='application/json')

    def post(self, request):
        shop = request.data.get('shop')
        serializer = AddShopSerializer(data=shop)
        if serializer.is_valid(raise_exception=True):
            shop_saved = serializer.save()
            return Response({'id': shop_saved.pk})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ErrorView(APIView):
    def get(self, request, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
