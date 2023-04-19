import requests


"""Работа к Cookies"""
payload = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', params=payload)

cookie_value = response1.cookies.get('auth_cookie') # получить cookies с названием auth_cookie

cookies = {}
if cookie_value is not None: # если куки пришли, используем их
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=cookies)
print(response2.text)


"""Отправка cookies на сервер"""
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are' : 'working'}
r = requests.get(url, cookies=cookies)
print(r.text)
print(r.cookies)  # использование cookies полученных от сервера
# print(r.cookies['example_cookie_name'])  # использование cookies полученных от сервера

