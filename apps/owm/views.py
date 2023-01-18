from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.owm.serializers import GetWeatherSerializer, WeatherSerializer
from utils.owm import OWMHelper

from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi


class WeatherView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GetWeatherSerializer

    @swagger_auto_schema(
        operation_description="Get actual weather data",
        method='get',
        query_serializer=GetWeatherSerializer(),
        responses={200: openapi.Response('', WeatherSerializer(many=True))},
        operation_id='current_weather_data'
    )
    @action(methods=['get'], detail=False)
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        owm = OWMHelper(**serializer.data)
        owm.get_owm_data()
        if owm.ok:
            response_serializer = WeatherSerializer(data=owm.transform_response())
            response_serializer.is_valid(raise_exception=True)
            return Response(response_serializer.data)
        raise NotFound(detail=owm.error(), code=404)
