import allure
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Create user")
class TestCreateUser(BaseClass):
    @allure.description("Test create user successfully")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Test create user with existing email")
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f'unexpected response {response.content}'

