from abc import ABC

from rest_framework import serializers

from .models import Shop


class CitySerializer(serializers.Serializer, ABC):
    name = serializers.CharField(max_length=255)


class StreetSerializer(serializers.Serializer, ABC):
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)


class ShopSerializer(serializers.Serializer, ABC):
    name = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)


class AddShopSerializer(serializers.Serializer, ABC):
    name = serializers.CharField(max_length=255)
    street_id = serializers.IntegerField()
    city_id = serializers.IntegerField()
    opens = serializers.TimeField()
    closes = serializers.TimeField()

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)
