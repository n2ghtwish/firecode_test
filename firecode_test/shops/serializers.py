from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class StreetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
