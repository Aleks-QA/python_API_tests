import requests
from apikey import API_TOKEN

""" Получить ответ от сайта(комплексный) """
params = {1: 1}
response = requests.get('https://www.google.com/search', params=params)

""" Получить статус код """
print(response.status_code)

""" Получить Headers(служебная информация) """
print(response.headers)

""" Получить содержимое страницы """
print(response.content)

""" Получить HTML код страницы """
print(response.text)

""" Получить в JSON формате """
print(response.json())

"""Get получить содержимое страницы"""
r = requests.get('http://example.com') #
print(r.text)


"""Передача параметров в запрос"""
url = 'http://example.com'
par = {'key1':'value1', 'key2':'value2'}
r = requests.get(url, params=par)
print(r.url)


"""Отправка cookies на сервер"""
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are' : 'working'}
r = requests.get(url, cookies=cookies)
print(r.text)
print(r.cookies['example_cookie_name'])  # использование cookies полученных от сервера


"""Пример POST"""

params = {"q": "Нижний Новгород", "appid": API_TOKEN, "units": "metric"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
}

data = {
"comments": "fefeefef",
"custemail": "esfsesefsefsefsefsef@dsffs.gh",
"custname": "login",
"custtel": "password",
}

variable = requests.Session() # Для обьединения запросов, куки сохраняются автоматически
variable.get('https://httpbin.org/form/post')


"""На этом ресурсе можно проверить как выглядит мой запрос"""
response = variable.post('https://httpbin.org/post',
                        headers=headers, data=data)  # allow_redirects=True разрешить перенаправление
x = response.text
print(x)
