import requests
from lib.logger import Logger



class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, method="POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, method="GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, method="PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, method="DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        send_url = f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_requests(url, data=data, headers=headers, cookies=cookies, method=method)

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
