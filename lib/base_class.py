import json.decoder
from datetime import datetime
import allure
import random
import string

from faker import Faker
from requests import Response


class BaseClass:
    def get_cookie(self, response: Response, cookie_name):
        """Find the cookie"""
        with allure.step(f"Find the cookie '{cookie_name}'"):
            assert cookie_name in response.cookies, f'\nCannot find cookie with name {cookie_name} in the last response\n'
            return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        """Find the header"""
        with allure.step(f"Find the header '{headers_name}'"):
            assert headers_name in response.headers, f'\nCannot find header with name {headers_name} in the last response\n'
            return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        """Check the format of the response, and the presence of the key"""
        with allure.step(f"Check the format of the response, and the presence of the key '{name}'"):
            try:
                response_as_dict = response.json()
            except json.decoder.JSONDecodeError:
                assert False, f'\nResponse is not in JSON format. Response text is "{response.text}"\n'

            assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"

            return response_as_dict[name]

    @staticmethod
    def random_data(localization='En', email=None, firstname=None, username=None, lastname=None,
                                  password=None, address=None, department=None):
        """Prepare registration information"""
        with allure.step(f"Get registration data"):
            faker = Faker(localization)
            random_part = datetime.now().strftime('%d%H%M%S')

            email: str = faker.email()
            first_name: str = faker.first_name()
            user_name: str = faker.first_name() + random_part
            last_name: str = faker.last_name()
            password: str = faker.password()
            address: str = faker.address()
            age = random.randint(10, 99)
            department: str = faker.job()

            data = {
                "email": email,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "user_name": user_name,
                "address": address,
                "age": age,
                "department": department
            }
            return data
