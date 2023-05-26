import allure
import pytest
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


class TestUserAgent:
    user_agent = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize("user_agent", user_agent)
    # def test_hello_call(self, name):
    def check_user_agent(self, user_agent):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check"'
        headers = {"User-Agent": user_agent}

        response = MyRequests.get(url=url, headers=headers)

        assert response.status_code == 200, 'status code not 200'

        print(response.text)

        # response_dict = response.json()
        # assert "answer" in response_dict, "There is no field 'answer' in the response"

        # if len(name) == 0:
        #     expected_response_text = 'Hello, someone'
        # else:
        #     expected_response_text = f'Hello, {name}'
        # actual_response_text = response_dict['answer']
        # assert actual_response_text == expected_response_text, 'Wrong response text'



#
# @allure.epic("Create user")
# class TestCreateUser(BaseClass):
#     random_data = BaseClass.random_data('ru')
#
#     data = {"password": random_data["password"],
#             "username": random_data["user_name"],
#             "firstName": random_data["first_name"],
#             "lastName": random_data["last_name"],
#             "email": random_data["email"]}
#
#     @allure.description("Test create user successfully")
#     def test_create_user_successfully(self):
#         response = MyRequests.post('/user/', data=self.data)
#
#         Assertions.assert_status_code(response, 200)
#         Assertions.assert_json_has_key(response, "id")
#
#     @allure.description("Test create user with existing email")
#     def test_create_user_with_existing_email(self):
#         email = "vinkotov@example.com"
#         data = self.data
#         data["email"] = email
#
#         response = MyRequests.post('/user/', data=data)
#
#         Assertions.assert_status_code(response, 400)
#         assert response.content.decode(
#             'utf-8') == f"Users with email '{email}' already exists", f'unexpected response {response.content}'