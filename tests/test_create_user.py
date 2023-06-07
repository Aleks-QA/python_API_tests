import allure
import pytest

from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Create user")
class TestCreateUser(BaseClass):
    random_data = BaseClass.random_data('ru')

    data = {"password": random_data["password"],
            "username": random_data["user_name"],
            "firstName": random_data["first_name"],
            "lastName": random_data["last_name"],
            "email": random_data["email"]}

    @allure.description("Test create user successfully")
    def test_create_user_successfully(self):
        response = MyRequests.post('/user/', data=self.data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Test create user with existing email")
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.data
        data["email"] = email

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            'utf-8') == f"Users with email '{email}' already exists", f'unexpected response {response.content}'

    data_invalid_email = {"password": random_data["password"],
            "username": random_data["user_name"],
            "firstName": random_data["first_name"],
            "lastName": random_data["last_name"],
            "email": "alexgmail.com"}

    data_empty_field = {"password": '',
            "username": random_data["user_name"],
            "firstName": random_data["first_name"],
            "lastName": random_data["last_name"],
            "email": random_data["email"]}

    data_one_character_name = {"password": random_data["password"],
            "username": random_data["user_name"],
            "firstName": 'a',
            "lastName": random_data["last_name"],
            "email": random_data["email"]}

    data_very_long_name = {"password": random_data["password"],
            "username": random_data["user_name"],
            "firstName": random_data["first_name"],
            "lastName": random_data["last_name"],
            "email": random_data["email"]}




    data_test_create_user = [
        ("invalid email", "alexgmail.com"),
        ("Firefox", 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0'),
        ("No",
         "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    ]

    @pytest.mark.parametrize("user_agent_platform", data_test_create_user)
    @allure.description("Test                   ")
    def test_check_user_agent_platform(self, user_agent_platform):
        url = '/user/'
        headers = {"User-Agent": user_agent_platform[1]}

        response = MyRequests.get(url=url, headers=headers)
        print(response.text)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, 'platform', user_agent_platform[0],
                                             "the platform is not correctly defined")
