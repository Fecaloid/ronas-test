from django.urls import path

from apps.owm.views import WeatherView

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather')
]
