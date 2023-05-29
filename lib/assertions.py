import allure
from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name_value, expected_value, error_massage): # Name - ключ по которому ищем
        """Comparison of the actual value with the expected value"""
        with allure.step(f"Comparison of the actual value with the expected value: key value '{name_value}' == '{expected_value}'"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert name_value in response_as_dict, f"\nResponse JSON doesn't have key '{name_value}'\n"
            error_massage_return = str(error_massage) + ': ' + response_as_dict[name_value] + ' != ' + expected_value
            assert response_as_dict[name_value] == expected_value, error_massage_return

    @staticmethod
    def assert_json_has_key(response: Response, name):
        """Checking for the presence of a key in a JSON response"""
        with allure.step(f"Checking for the presence of a key '{name}' in a JSON response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        """Checking for keys in the JSON response"""
        with allure.step(f"Checking for '{names}' keys in the JSON response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            for name in names:
                assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        """Checking that there is NO KEY in the JSON response"""
        with allure.step(f"Checking that there is NO KEY: '{name}' in the JSON response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert name not in response_as_dict, f"\nJSON response must not contain a key '{name}'\n"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        """Comparison of the actual code status with the expected value"""
        with allure.step(f"Comparison of the actual code status with the expected value '{expected_status_code}'"):
            assert response.status_code == expected_status_code, \
                f"\nUnexpected status code! Expected: {expected_status_code}, Actual {response.status_code}\n"
