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
    deg = serializers.IntegerField()
    gust = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    direction = serializers.CharField(max_length=3)

    class Meta:
        fields = '__all__'


class WeatherSerializer(serializers.Serializer):
    wind = WindSerializer()
    temp_fahrenheit = serializers.DecimalField(max_digits=5, decimal_places=2)
    temp_celsius = serializers.DecimalField(max_digits=5, decimal_places=2)
    description = serializers.CharField(max_length=255)
    icon = serializers.CharField(max_length=3)
    humidity = serializers.IntegerField()
    pressure_hpa = serializers.IntegerField()
    pressure_mmhg = serializers.DecimalField(max_digits=6, decimal_places=2)
    pop = serializers.IntegerField()

    class Meta:
        fields = '__all__'
