import json
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PeeweeCity, PeeweeStreet, PeeweeShop
from .serializers import PeeWeeShopValidator


class PeeWeeCityView(APIView):
    def get(self, request):
        cities = list(PeeweeCity.select(PeeweeCity.name).dicts())
        return Response(json.dumps({'peewee_cities': cities}, ensure_ascii=False,
                                   indent=4), content_type='application/json')


class PeeWeeStreetView(APIView):
    def get(self, request):
        if 'city_id' in request.query_params.keys():
            city_id = int(request.query_params['city_id'])
            streets = list(PeeweeStreet.select(PeeweeStreet.name).where(PeeweeStreet.city == city_id).dicts())
        else:
            streets = list(PeeweeStreet.select(PeeweeStreet.name).dicts())
        return Response(json.dumps({'peewee_cities': streets}, ensure_ascii=False,
                                   indent=4), content_type='application/json')


class PeeWeeShopView(APIView):
    def get(self, request):
        shops = PeeweeShop.select()\
            .join(PeeweeCity, on=(PeeweeShop.city == PeeweeCity.id))\
            .join(PeeweeStreet, on=(PeeweeShop.street == PeeweeStreet.id))
        if len(request.query_params) > 0:
            if 'city' in request.query_params.keys():
                city_id = int(request.query_params['city'])
                shops = shops.select().where(PeeweeShop.city == city_id)
            if 'street' in request.query_params.keys():
                street_id = int(request.query_params['street'])
                shops = shops.select().where(PeeweeShop.street == street_id)
            if 'open' in request.query_params.keys():
                ct = datetime.now().time()
                if request.query_params['open'] == '0':
                    shops = shops.select().where((PeeweeShop.opens > ct) | (PeeweeShop.closes < ct))
                elif request.query_params['open'] == '1':
                    shops = shops.select().where(PeeweeShop.opens < ct, PeeweeShop.closes > ct)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        shops = list(shops.select(PeeweeShop.name,
                                  PeeweeCity.name.alias('city'),
                                  PeeweeStreet.name.alias('street')).dicts())
        return Response(json.dumps({'peewee_cities': shops}, ensure_ascii=False,
                                   indent=4), content_type='application/json')

    def post(self, request):
        shop = request.data
        validator = PeeWeeShopValidator()
        validator.validate(shop)
        if validator.errors == {}:
            new_shop = PeeweeShop.create(name=validator.data['name'],
                                         city=validator.data['city'],
                                         street=validator.data['street'],
                                         building=validator.data['building'],
                                         opens=validator.data['opens'],
                                         closes=validator.data['closes'],
                                         )
            return Response({'id': new_shop.id})
        else:
            return Response(json.dumps({'errors': validator.errors}, ensure_ascii=False, indent=4),
                            content_type='application/json', status=status.HTTP_400_BAD_REQUEST)


class ErrorView(APIView):
    def get(self, request, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
