from unittest import mock

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

from tests.mocks.owm_mock import mock_transform_response, OWMMockResponse


@mock.patch("requests.get", return_value=OWMMockResponse())
class AppsOWMApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.request = {"city": "Одесса", "country_code": 'ua', 'language_code': 'ru'}

    def test_get_task_list(self, mocked):
        response = self.client.get(reverse('weather'), data=self.request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), mock_transform_response)
