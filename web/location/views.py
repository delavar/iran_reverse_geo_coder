import io

import django_filters
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from location.models import City, Province, County
from location.serializers import CitySerializer, CountySerializer, ProvinceSerializer, SearchSerializer, \
    FullCitySerializer
import reverse_geocoder as rg


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    queryset = Province.active_objects.all()
    serializer_class = ProvinceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    filterset_fields = ('province',)
    queryset = County.active_objects.all()
    serializer_class = CountySerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    filterset_fields = ('province', 'county')
    queryset = City.active_objects.all()
    serializer_class = CitySerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class SearchView(views.APIView):
    serializer_class = SearchSerializer

    def get(self, request):

        serializer = SearchSerializer(data=request.GET)
        response = {'data': {}}
        try:
            serializer.is_valid(raise_exception=True)
            location = [float(x) for x in serializer.data.get('place', '').split(',')]
            if (len(location) != 2):
                raise Exception()
        except:
            response['data'] = {"place": "for example place=23.2333,34.6666"}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

        rg.RGeocoder(mode=2, verbose=True,
                     stream=io.StringIO(open('location/city_reverse_geo.csv', encoding='utf-8').read()))
        coordinates = (location[0], location[1]),
        results = rg.search(coordinates)

        ids = []
        for result in results:
            ids.append(result['name'])

        cities = City.objects.filter(pk__in=ids)
        data = FullCitySerializer(instance=cities, many=True,
                                  read_only=True).data
        response['data'] = data
        return Response(data=response, status=status.HTTP_200_OK, content_type='application/json')
