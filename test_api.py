import requests


# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

def test_get_locations_for_us_90210_check_status_code_equals_200():
    """Проверка статус кода"""
    response = requests.get("http://api.zippopotam.us/us/90210")
    print(response.json())
    assert response.status_code == 200


def test_get_locations_for_us_90210_check_content_type_equals_json():
    """Проверка значения заголовка"""
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers['Content-Type'] == "application/json"


def test_get_locations_for_us_90210_check_country_equals_united_states():
    """Проверка элементов тела ответа, соответствия ключа: значению"""
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"


def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    """Проверка элемента тела на соответствие"""
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"


def test_get_locations_for_us_90210_check_one_place_is_returned():
    """Проверка, что список мест, возвращенных API, содержит ровно одну запись"""
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert len(response_body["places"]) == 1
