import json

string_as_json_format = '{"answer": "Hello, User"}'  # входная строка, ключ-значение должны быть в двойных кавычках!

obj = json.loads(string_as_json_format)  # превращаем строку в объект JSON

key = "answer"


"""Поиск значения по ключу"""
if key in obj:
    print(obj[key])
else:
    print(f'Ключа {key} в JSON нет')
