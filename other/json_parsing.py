import json
import requests
from json.decoder import JSONDecodeError


string_as_json_format = '{"answer": "Hello, User"}'  # входная строка, ключ-значение должны быть в двойных кавычках!
obj = json.loads(string_as_json_format)  # превращаем строку в объект JSON
key = "answer"


"""Поиск значения по ключу"""
if key in obj:
    print(obj[key])
else:
    print(f'Ключа {key} в JSON нет')


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

