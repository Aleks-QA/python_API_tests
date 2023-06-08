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

    @allure.step("Get random data")
    def get_random_data(self):
        random_data = BaseClass.random_data('ru')
        data = {"password": random_data["password"],
                "username": random_data["user_name"],
                "firstName": random_data["first_name"],
                "lastName": random_data["last_name"],
                "email": random_data["email"]}
        return data

    @pytest.mark.parametrize("field", ["password", "username", "firstName", "lastName", "email"])
    @pytest.mark.parametrize("invalid_data", ['', 's', 'not_available', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])
    @allure.description("Test registration of a new user with invalid data")
    def test_create_user_with_invalid_data(self, field, invalid_data):
        """test with an empty field, test with a field of 1 character,
         test with more than 250 characters, test registration with no required field"""
        test_data = self.get_random_data()

        if invalid_data == 'not_available':
            test_data.pop(field)
        else:
            test_data[field] = invalid_data

        response = MyRequests.post('/user/', data=test_data)

        Assertions.assert_status_code(response, 400)
