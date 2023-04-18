import requests
from json.decoder import JSONDecodeError


"""Поиск значения по ключу в входных данных в формате JSON"""
payload = {"name": "Alex"}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
parsed_response_text = response.json()
print(parsed_response_text['answer'])


"""Поиск значения по ключу в входных данных НЕ зная формат"""
response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")


"""Работа к Cookies"""
payload = {"login":"secret_login", "password":"secret_pass"}
response = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', params=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies)) # получить cookies


