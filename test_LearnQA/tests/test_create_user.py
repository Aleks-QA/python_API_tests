import requests
import pytest
from test_LearnQA.lib.base_class import BaseClass
from test_LearnQA.lib.assertions import Assertions
from datetime import datetime


class TestCreateUser(BaseClass):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post('https://playground.learnqa.ru/api/user/', params=data)  # params==data

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = requests.post('https://playground.learnqa.ru/api/user/', params=data)  # params==data

        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f'unexpected response {response.content}'






