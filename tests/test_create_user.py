import allure
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Create user")
class TestCreateUser(BaseClass):
    random_data = BaseClass.random_data('ru')

    data = {
        "password": random_data["password"],
        "username": random_data["user_name"],
        "firstName": random_data["first_name"],
        "lastName": random_data["last_name"],
        "email": random_data["email"]
    }

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
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f'unexpected response {response.content}'

