import json.decoder
from datetime import datetime
import allure
import random
from faker import Faker


class BaseClass:
    """Содержит ключевые методы которые вынесены в родительский класс для пере-использования в тестах"""
    def get_cookie(self, response, cookie_name):
        """Find the cookie and get the value"""
        with allure.step(f"Find the cookie '{cookie_name}'"):
            assert cookie_name in response.cookies, f'\nCannot find cookie with name {cookie_name} in the last response\n'
            return response.cookies[cookie_name]

    def get_header(self, response, headers_name):
        """Find the header and get the value"""
        with allure.step(f"Find the header '{headers_name}'"):
            assert headers_name in response.headers, f'\nCannot find header with name {headers_name} in the last response\n'
            return response.headers[headers_name]

    def get_json_value(self, response, name):
        """Check the format of the response, and the presence of the key"""
        with allure.step(f"Check the format of the response, and the presence of the key '{name}'"):
            try:
                response_as_dict = response.json()
            except json.decoder.JSONDecodeError:
                assert False, f'\nResponse is not in JSON format. Response text is "{response.text}"\n'

            assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"
            return response_as_dict[name]

    @staticmethod
    def random_data(localization='En', email=None, firstname=None, username=None, lastname=None, address=None,
                    password=None, job=None):
        """Prepare registration information"""
        # EXAMPLE OF USE IN TESTS
        # from lib.base_class import BaseClass
        #
        # random_data = BaseClass.random_data('ru')
        # data = {"username": random_data["user_name"],
        #         "email": random_data["email"]}

        with allure.step(f"Get registration data"):
            faker = Faker(localization)
            random_part = datetime.now().strftime('%d%H%M%S')

            data = {
                "email": faker.email(),
                "password": faker.password(),
                "first_name": faker.first_name(),
                "last_name": faker.last_name(),
                "user_name": faker.first_name() + random_part,
                "address": faker.address(),
                "age": random.randint(18, 99),
                "job": faker.job()
            }
            return data
