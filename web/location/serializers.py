from rest_framework import serializers

from location.models import Province, County, City


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'name')
        read_only_fields = []


class CountySerializer(serializers.ModelSerializer):
    # province = ProvinceSerializer(read_only=True)

    class Meta:
        model = County
        fields = ('id', 'name', 'province_id')
        read_only_fields = []


class CitySerializer(serializers.ModelSerializer):
    # province = ProvinceSerializer(read_only=True)
    # county = CountySerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'county_id', 'province_id')
        read_only_fields = []


class MiniProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('name',)
        read_only_fields = []


class MiniCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('name',)
        read_only_fields = []


class FullCitySerializer(serializers.ModelSerializer):
    province = MiniProvinceSerializer(read_only=True)
    county = MiniCountySerializer(read_only=True)

    class Meta:
        model = City
        fields = ('name', 'lat', 'lng', 'county', 'province')
        read_only_fields = []


class SearchSerializer(serializers.Serializer):
    place = serializers.CharField(required=True)
