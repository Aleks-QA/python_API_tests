import requests
from apikey import API_TOKEN

params = {"q" : "Нижний Новгород", "appid" : API_TOKEN, "units" : "metric"}

response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

x = response.json()
print(f'В городе {x["name"]}, температура от {x["main"]["temp_min"]}, до {x["main"]["temp_max"]}')

