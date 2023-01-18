import json
from os.path import join

from config.settings import BASE_DIR


class OWMMockResponse:
    """
    Mocked openweathermap response
    """
    def __init__(self):
        self.status_code = 200
        self.path = join(BASE_DIR, 'tests/fixtures/owm_mock.json')

    @staticmethod
    def ok():
        return True

    def json(self):
        with open(self.path, 'r') as f:
            return json.load(f)


mock_transform_response = {
    "wind": {
        "speed": 9.36,
        "deg": 190,
        "gust": 17.68,
        "direction": "S"
    },
    "temp_fahrenheit": 48.96,
    "temp_celsius": 9.42,
    "description": "облачно с прояснениями",
    "icon": "04n",
    "humidity": 85,
    "pressure_hpa": 1006,
    "pressure_mmhg": 754.56,
    "pop": 0
}
