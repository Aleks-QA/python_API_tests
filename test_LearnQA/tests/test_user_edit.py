import requests
from test_LearnQA.lib.base_class import BaseClass
from test_LearnQA.lib.assertions import Assertions


class TestGetUser(BaseClass):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        username = register_data["username"]
        first_name = register_data["firstName"]
        last_name = register_data["lastName"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_date = {
            "email": email,
            "password": password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_date)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "changed name"

        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid},
                                 data={"firstName":new_name}
                                 )

        Assertions.assert_status_code(response3, 200)

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid},
                                 )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )