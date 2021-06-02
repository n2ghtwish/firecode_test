import peewee_validates as pv

from rest_framework import serializers

from .models import Shop, PeeWeeShop


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class StreetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)


class AddShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    street_id = serializers.IntegerField()
    city_id = serializers.IntegerField()
    opens = serializers.TimeField()
    closes = serializers.TimeField()

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)


class PeeWeeShopValidator(pv.ModelValidator):
    name = pv.StringField(max_length=255)
    street_id = pv.IntegerField()
    city_id = pv.IntegerField()
    building = pv.StringField(max_length=10)
    opens = pv.TimeField()
    closes = pv.TimeField()

    def create(self, validated_data):
        return PeeWeeShop.create(**validated_data)
