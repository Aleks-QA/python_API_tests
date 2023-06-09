import requests
from lib.logger import Logger
import allure
from environment import ENV_OBJECT


class MyRequests:
    """
    Это вспомогательный класс обертка, внутри этого класса происходят сами запросы,
    Необходим для того, чтобы в тестах напрямую не использовать requests,
    Благодаря этому происходит надежное построение отчетов.
    """
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"POST request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, method="POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, method="GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, method="PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, method="DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        http = "http"
        if http in url:
            send_url = url
        else:
            send_url = f"{ENV_OBJECT.get_base_url()}{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_requests(send_url, data=data, headers=headers, cookies=cookies, method=method)

        if method == "GET":
            response = requests.get(send_url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(send_url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(send_url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(send_url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        Logger.add_response(response)

        return response
