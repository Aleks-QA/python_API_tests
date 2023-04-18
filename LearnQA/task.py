import requests


# # payload = {"login":"secret_login", "password":"secret_pass"}
# response = requests.post('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
# print(response.url)
# print(response.history)


# payload = {"method": "POST"}
payload = {"method": "GET"} # работает с delete в этом случае
# payload = {"method": "HEAD"}
# payload = {"method": "PUT"}
# payload = {"method": "DELETE"}

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=payload)
# response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', params=payload)
# response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', params=payload)
# response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', params=payload)
print(response.text)
print(response.url)






