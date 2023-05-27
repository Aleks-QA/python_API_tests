import allure
import pytest
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Check user agent")
class TestUserAgent(BaseClass):
    user_agent = [
        ("Android", "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30"
                    " (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("iOS", 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                ' CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ("Unknown", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        ]

    @pytest.mark.parametrize("user_agent", user_agent)
    @allure.description("Test check user agent")
    def test_check_user_agent(self, user_agent):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        headers = {"User-Agent": user_agent[1]}

        response = MyRequests.get(url=url, headers=headers)

        Assertions.assert_json_value_by_name(response, 'device', user_agent[0], "the platform is not correctly defined")
        Assertions.assert_status_code(response, 200)
