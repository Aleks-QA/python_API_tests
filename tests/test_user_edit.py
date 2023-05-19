import allure
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Edit user")
class TestGetUser(BaseClass):
    random_data = BaseClass.random_data('ru')

    data = {"password": random_data["password"],
            "username": random_data["user_name"],
            "firstName": random_data["first_name"],
            "lastName": random_data["last_name"],
            "email": random_data["email"]}

    @allure.description("Test edit user")
    def test_edit_just_created_user(self):
        with allure.step(f"REGISTER"):
            """REGISTER"""
            register_data = self.data
            response1 = MyRequests.post("/user/", data=self.data)

            Assertions.assert_status_code(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data["email"]
            password = register_data["password"]
            user_id = self.get_json_value(response1, "id")

        with allure.step(f"LOGIN"):
            """LOGIN"""
            login_date = {"email": email, "password": password}
            response2 = MyRequests.post("/user/login", data=login_date)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step(f"EDIT"):
            """EDIT"""
            new_name = "changed name"
            response3 = MyRequests.put(f"/user/{user_id}",
                                       headers={"x-csrf-token": token},
                                       cookies={"auth_sid": auth_sid},
                                       data={"firstName": new_name})
            Assertions.assert_status_code(response3, 200)

        with allure.step(f"GET"):
            """GET"""
            response4 = MyRequests.get(f"/user/{user_id}",
                                       headers={"x-csrf-token": token},
                                       cookies={"auth_sid": auth_sid})
            Assertions.assert_status_code(response4, 200)
            Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

        with allure.step(f"DELETE"):
            """DELETE"""
            response5 = MyRequests.delete(f'/user/{user_id}',
                                          headers={"x-csrf-token": token},
                                          cookies={"auth_sid": auth_sid})
            Assertions.assert_status_code(response5, 200)

        with allure.step(f"CHECK DELETE"):
            """CHECK DELETE"""
            response6 = MyRequests.get(f"/user/{user_id}",
                                       headers={"x-csrf-token": token},
                                       cookies={"auth_sid": auth_sid})
            Assertions.assert_status_code(response6, 404)
