import requests
import json



class TestGoogleMaps():
    data = {
      "location": {
        "lat": -40.383494,
        "lng": 30.427362
      },
      "accuracy": 50,
      "name": "Frontline house",
      "phone_number": "(+91) 983 111 1111",
      "address": "1, test address",
      "types": [
        "shoe park",
        "shop"
      ],
      "website": "http://google.com",
      "language": "French-IN"
    }

    params = {
        "key": "qaclick123"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    def test_create_place(self):
        """Проверка статус кода"""
        response = requests.post("https://rahulshettyacademy.com/maps/api/place/add/json", data=self.data, params=self.params, headers=self.headers)
        # response.encoding = 'utf-8-sig'
        # print(response.json())
        print(response.text)


        assert response.status_code == 200







