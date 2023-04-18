import requests


class TestFirstApi:
    def test_hello_call(self):
        url = 'https://playground.learnqa.ru/api/hello'
        name = "Alex"
        data = {"name": name}

        response = requests.get(url=url, params=data)
        assert response.status_code == 200, 'status code not 200'

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f'Hello, {name}'
        actual_response_text = response_dict['answer']
        assert actual_response_text == expected_response_text, 'Wrong response text'












