import requests

from config.settings import OWM_ENDPOINT, OWM_API_KEY


class OWMHelper:
    """
    openweathermap helper.
    Can get data from resource, transform this data for serializer or return error text
    """
    def __init__(self, city: str, country_code: str, language_code: str):
        """
        Get actual data from openweathermap.

        Arguments:
            city: City name.
            country_code: City country code.
            language_code: Language code.
        """
        self.response: requests.Response | None = None
        self.data: dict | None = None
        self.city = city
        self.country_code = country_code
        self.language_code = language_code
        self.ok = False

    def _build_url(self) -> str:
        """
        Create openweathermap request url
        """
        return f"{OWM_ENDPOINT}forecast?q={self.city}, {self.country_code}" \
               f"&appid={OWM_API_KEY}&lang={self.language_code}&units=metric"

    def get_owm_data(self):
        """
        send request to owm. Save response
        """
        url = self._build_url()
        self.response = requests.get(url)
        if self.response.ok:
            self.ok = True
            self.data = self.response.json()['list'][0]

    def _get_pop(self) -> float | None:
        """
        Find and return value of Probability of precipitation
        """
        pop = self.data.get('pop', 0)
        return pop * 100

    def transform_response(self) -> dict:
        """
        Transform openweathermap response to dict for
        /app/owm/serializers/WeatherSerializer if request success.
        Or return error message text
        """
        data = self.data
        if self.ok:
            wind = data.get('wind', {})
            if wind:
                wind['direction'] = deg_to_compass(wind['deg'])

            result = {
                "wind": wind,
                "temp_fahrenheit": celsius_to_fahrenheit(data['main']['temp']),
                "temp_celsius": data['main']['temp'],
                "description": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon'],
                "humidity": data['main']['humidity'],
                "pressure_hpa": data['main']['pressure'],
                "pressure_mmhg": hpa_to_mmhg(data['main']['pressure']),
                "pop": self._get_pop(),
            }
            return result

    def error(self):
        return self.data.get("message", "Undefined error")


def deg_to_compass(value: int) -> str:
    result = int((value/22.5)+.5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return arr[(result % 16)]


def celsius_to_fahrenheit(value: float) -> float:
    result = (value * 1.8) + 32
    return round(result, 2)


def hpa_to_mmhg(value: int) -> float:
    result = value * 0.75006375541921
    return round(result, 2)
