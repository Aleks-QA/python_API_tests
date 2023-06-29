import allure
import requests
from requests import Response
from environment import ENV_OBJECT
from lib.logger import Logger

"""
ОПИСАНИЕ И ПРИМЕР РАБОТЫ ДАННОГО ПРОЕКТА

lib/assertion.py - содержит вспомогательные функции сравнения
которые на вход получают ответ от сервера и ожидаемое значение
парсят из ответа фактические значения и сравнивают их

lib/base_class.py - содержит ключевые методы которые вынесены в родительский класс для пере-использования в тестах,
такие методы как, получение данных запроса(заголовки, куки и работа с телом запроса) и генерацию тестовых данных

lib/my_request.py - содержит вспомогательный класс обертку, внутри этого класса происходят сами запросы,
необходим для того, чтобы в тестах напрямую не использовать requests, это даст более надежное построение отчетов

tests/ - содержит тесты, описанные бизнес-логикой

environment.py - вспомогательный скрипт который возвращает домен в зависимости от того,
на каком окружении мы хотим запускать тесты

"""


# -------------------------------------------   lib/base_class.py    ----------------------------------------------

class BaseClassExample:
    """
    Содержит ключевые методы которые вынесены в родительский класс для пере-использования в тестах,
    такие методы как, получение данных запроса(заголовки, куки и работа с телом запроса) и генерацию тестовых данных
    """
    def get_header(self, response: Response, headers_name):
        """Find the header and get the value"""
        assert headers_name in response.headers, f'\nCannot find header with name {headers_name} in the last response\n'
        return response.headers[headers_name]


# -------------------------------------------   tests/test_example.py    ---------------------------------------------

class TestGetUser(BaseClassExample):  # 708 vs 1013
    """
    tests/ - СОДЕРЖИТ ТЕСТЫ, ОПИСАННЫЕ БИЗНЕС-ЛОГИКОЙ ТЕСТ-КЕЙСОВ
    ШАГИ:
    1 - Получить информацию о пользователе по id, без авторизации
    2 - Убедиться что статус код - 200
    3 - Убедиться что в ответе есть поле "username" и имеет значение "Lana"
    4 - Убедиться что в ответе отсутствуют недоступные для неавторизованного пользователя данные
    5 - Убедиться что заголовок ответа "Content-Type" имеет значение "application/json"
    """

    """ СРАВНЕНИЕ ОБЪЕМА КОДА БЕЗ УЧЕТА ПОДКЛЮЧЕНИЯ ОТЧЕТОВ И КОММЕНТАРИЕВ, 708 CИМВОЛОВ VS 1013 CИМВОЛОВ """
    def test_get_user_details_not_auth(self):
        """Построение тестов на основе данного фреймворка"""
        headers = {"Content-Type": 'application/json'}
        # Получить информацию о пользователе по id, без авторизации
        response = MyRequestsExample.get("/user/1", headers=headers)

        # Убедиться что статус код - 200
        AssertionsExample.assert_status_code(response, 200)

        # Убедиться что в ответе есть поле "username" и имеет значение "Lana"
        AssertionsExample.assert_json_has_key(response, "username")
        AssertionsExample.assert_json_value_by_name(response, 'username', 'Lana', 'invalid value')

        # Убедиться что в ответе отсутствуют недоступные для неавторизованного пользователя данные
        AssertionsExample.assert_json_has_not_key(response, "email")
        AssertionsExample.assert_json_has_not_key(response, "firstname")
        AssertionsExample.assert_json_has_not_key(response, "lastname")

        # Убедиться что заголовок ответа "Content-Type" имеет значение "application/json
        actual_header = BaseClassExample.get_header(self, response, 'Content-Type')
        assert actual_header == 'application/json', 'invalid header'

    def test_get_user_details_not_auth_old(self):
        """Построение тестов БЕЗ использования данного фреймворка"""
        url = "https://playground.learnqa.ru/api/user/1"
        headers = {"Content-Type": 'application/json'}
        # Получить информацию о пользователе по id, без авторизации
        response = requests.get(url, headers=headers)

        # Убедиться что статус код - 200
        status_code = response.status_code
        assert status_code == 200, f"\nUnexpected status code! Expected: 200, Actual {response.status_code}\n"

        # Убедиться что в ответе есть поле "username" и имеет значение "Lana"
        response_as_dict = response.json()
        name_header = "username"
        assert name_header in response_as_dict, f"\nResponse JSON doesn't have key '{name_header}'\n"
        assert "Lana" == response_as_dict[name_header], "invalid value"

        # Убедиться что в ответе отсутствуют недоступные для неавторизованного пользователя данные
        assert "email" not in response_as_dict, f"\nJSON response must not contain a key '{name_header}'\n"
        assert "firstname" not in response_as_dict, f"\nJSON response must not contain a key '{name_header}'\n"
        assert "lastname" not in response_as_dict, f"\nJSON response must not contain a key '{name_header}'\n"

        # Убедиться что заголовок ответа "Content-Type" имеет значение "application/json
        actual_header = response.headers["Content-Type"]
        assert actual_header == 'application/json', 'invalid header'


# -------------------------------------------   lib/my_request.py    ----------------------------------------------

class MyRequestsExample:
    """
    Это вспомогательный класс обертка, внутри этого класса происходят сами запросы
    Необходим для того, чтобы в тестах напрямую не использовать requests
    Что даст более надежное построение отчетов
    """
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to URL '{url}'"):
            return MyRequestsExample._send(url, data, headers, cookies, method="GET")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        send_url = f"{ENV_OBJECT.get_base_url()}{url}"
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_requests(send_url, data=data, headers=headers, cookies=cookies, method=method)
        if method == "GET":
            response = requests.get(send_url, params=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")
        Logger.add_response(response)

        return response


# -------------------------------------------   lib/assertion.py    ----------------------------------------------

class AssertionsExample:
    """
    Содержит вспомогательные функции сравнения
    которые на вход получают ответ от сервера и ожидаемое значение,
    парсят из ответа фактические значения и сравнивают их
    """
    @staticmethod
    def assert_json_value_by_name(response: Response, name_value, expected_value, error_massage): # Name - ключ по которому ищем
        """Comparison of the actual value with the expected value"""
        response_as_dict = response.json()

        assert name_value in response_as_dict, f"\nResponse JSON doesn't have key '{name_value}'\n"
        error_massage_return = str(error_massage) + ': ' + str(response_as_dict[name_value]) + ' != ' + str(expected_value)
        assert expected_value == response_as_dict[name_value], error_massage_return

    @staticmethod
    def assert_json_has_key(response: Response, name):
        """Checking for the presence of a key in a JSON response"""
        response_as_dict = response.json()

        assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        """Checking that there is NO KEY in the JSON response"""
        response_as_dict = response.json()

        assert name not in response_as_dict, f"\nJSON response must not contain a key '{name}'\n"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        """Comparison of the actual code status with the expected value"""
        assert response.status_code == expected_status_code, \
            f"\nUnexpected status code! Expected: {expected_status_code}, Actual {response.status_code}\n"
