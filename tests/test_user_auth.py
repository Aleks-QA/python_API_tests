import pytest
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests
import allure


@allure.epic("Authorization cases")
class TestUserAuth(BaseClass):
    def setup_method(self):
        """Авторизация и сохранение токена, куки и ID пользователя для следующих тестов"""
        data = {"email": 'vinkotov@example.com',
                "password": "1234"}
        response1 = MyRequests.post('/user/login', data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.description("This test successfully authorizes the user by token and cookie")
    def test_auth_user(self):
        """Данный тест успешно авторизует пользователя по токену и cookie"""
        response2 = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token}, cookies={"auth_sid": self.auth_sid})
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from method is not equal to user id from check method")

    exclude_params = [("no_cookies"), ("no_token")]

    @allure.description("This test checks authorization status w/o sending auth cookies or token")
    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        """Этот тест проверяет статус авторизации без отправки cookies или токена auth"""
        if condition == 'no_cookies':
            response2 = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token})
        else:
            response2 = MyRequests.get("/user/auth", cookies={"auth_sid": self.auth_sid})
        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorized with condition {condition}")
