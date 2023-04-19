import requests


class MyRequests():
    @staticmethod
    def post(url: str, data: dict = None, headers: dict  = None, cookies: dict  = None):
        return MyRequests._send(url, data, headers, cookies, method="POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict  = None, cookies: dict  = None):
        return MyRequests._send(url, data, headers, cookies, method="GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict  = None, cookies: dict  = None):
        return MyRequests._send(url, data, headers, cookies, method="PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict  = None, cookies: dict  = None):
        return MyRequests._send(url, data, headers, cookies, method="DELETE")


    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(url,params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.get(url,data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.get(url,data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.get(url,data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response









