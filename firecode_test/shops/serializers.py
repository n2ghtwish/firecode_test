import peewee_validates as pv
from rest_framework import serializers
from .models import Shop


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


class PeeWeeShopValidator(pv.Validator):
    name = pv.StringField(validators=[pv.validate_required(),
                                      pv.validate_not_empty(),
                                      pv.validate_length(low=1, high=255)])
    street = pv.IntegerField(validators=[pv.validate_required(), pv.validate_not_empty()])
    city = pv.IntegerField(validators=[pv.validate_required(), pv.validate_not_empty()])
    building = pv.StringField(validators=[pv.validate_required(),
                                          pv.validate_not_empty(),
                                          pv.validate_length(low=1, high=10)])
    opens = pv.TimeField(validators=[pv.validate_required(), pv.validate_not_empty()])
    closes = pv.TimeField(validators=[pv.validate_required(), pv.validate_not_empty()])
