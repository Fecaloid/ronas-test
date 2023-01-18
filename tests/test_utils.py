from django.test import TestCase
from unittest import mock

from config.settings import OWM_ENDPOINT, OWM_API_KEY
from tests.mocks.owm_mock import OWMMockResponse, mock_transform_response
from utils.owm import OWMHelper, deg_to_compass, celsius_to_fahrenheit, hpa_to_mmhg


@mock.patch("requests.get", return_value=OWMMockResponse())
class UtilsTest(TestCase):
    def setUp(self) -> None:
        self.request = {"city": "Одесса", "country_code": 'ua', 'language_code': 'ru'}
        self.owm = OWMHelper(**self.request)

    def test_owm_request_data(self, mocked):
        self.assertEqual(self.owm.city, self.request['city'])
        self.assertEqual(self.owm.country_code, self.request['country_code'])
        self.assertEqual(self.owm.language_code, self.request['language_code'])

    def test_owm_build_url(self, mocked):
        url = f"{OWM_ENDPOINT}forecast?q={self.request['city']}, {self.request['country_code']}" \
              f"&appid={OWM_API_KEY}&lang={self.request['language_code']}&units=metric"
        self.assertEqual(self.owm._build_url(), url)

    def test_owm_get_owm_data(self, mocked):
        self.owm.get_owm_data()
        mocked_data = OWMMockResponse()
        self.assertEqual(self.owm.response.json(), mocked_data.json())

    def test_owm_get_pop(self, mocked):
        self.owm.get_owm_data()
        self.owm.data['pop'] = 0.17
        self.assertEqual(self.owm._get_pop(), 17)

    def test_owm_transform_response(self, mocked):
        self.owm.get_owm_data()
        self.assertEqual(self.owm.transform_response(), mock_transform_response)

    def test_owm_deg_to_compass(self, mocked):
        self.assertEqual(deg_to_compass(190), 'S')

    def test_owm_celsius_to_fahrenheit(self, mocked):
        self.assertEqual(celsius_to_fahrenheit(9.42), 48.96)

    def test_owm_hpa_to_mmhg(self, mocked):
        self.assertEqual(hpa_to_mmhg(1006), 754.56)
