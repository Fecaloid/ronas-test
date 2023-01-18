from rest_framework import serializers

from config.settings import DEFAULT_COUNTRY_CODE, DEFAULT_LANGUAGE_CODE


class GetWeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=255, label="City name", help_text="City name")
    country_code = serializers.CharField(max_length=2, default=DEFAULT_COUNTRY_CODE)
    language_code = serializers.CharField(max_length=2, default=DEFAULT_LANGUAGE_CODE)

    class Meta:
        fields = '__all__'


class WindSerializer(serializers.Serializer):
    speed = serializers.DecimalField(max_digits=5, decimal_places=2, help_text="Wind speed")
    deg = serializers.IntegerField(help_text="Wind direction in deg")
    gust = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    direction = serializers.CharField(max_length=3, help_text="Wind direction code")

    class Meta:
        fields = '__all__'


class WeatherSerializer(serializers.Serializer):
    wind = WindSerializer(help_text="Wind data")
    temp_fahrenheit = serializers.DecimalField(max_digits=5, decimal_places=2, help_text="Temperature in fahrenheit")
    temp_celsius = serializers.DecimalField(max_digits=5, decimal_places=2, help_text="Temperature in celsius")
    description = serializers.CharField(max_length=255, help_text="Short weather description")
    icon = serializers.CharField(max_length=3, help_text="Weatehr icon code")
    humidity = serializers.IntegerField(help_text="Humidity")
    pressure_hpa = serializers.IntegerField(help_text="Pressure in hpa")
    pressure_mmhg = serializers.DecimalField(max_digits=6, decimal_places=2, help_text="Pressure in mmhg")
    pop = serializers.IntegerField(help_text="Probability of precipitation in %")

    class Meta:
        fields = '__all__'
