import allure
import pytest
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Check user agent")
class TestUserAgent(BaseClass):
    """
    Проверка определения параметров клиента по строке заголовка User Agent,
    на вход подаем по паре параметров(ожидаемое значение параметра и входное значение)
    """
    user_agent_device = [
        ("iOS", 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                ' CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ("Android", "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30"
                    " (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Unknown", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    ]

    @pytest.mark.parametrize("user_agent_device", user_agent_device)
    @allure.description("Test check user agent - device")
    def test_check_user_agent_device(self, user_agent_device):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        headers = {"User-Agent": user_agent_device[1]}

        response = MyRequests.get(url=url, headers=headers)

        Assertions.assert_status_code(response, 200)
        # Метод работает с JSON ответом, ищет значение по ключу и сравнивает его с ожидаемым
        Assertions.assert_json_value_by_name(response, 'device', user_agent_device[0],
                                             "the device is not correctly defined")

    user_agent_platform = [
        ("Mobile", 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                   'CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ("Web", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
    ]

    @pytest.mark.parametrize("user_agent_platform", user_agent_platform)
    @allure.description("Test check user agent - platform")
    def test_check_user_agent_platform(self, user_agent_platform):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        headers = {"User-Agent": user_agent_platform[1]}

        response = MyRequests.get(url=url, headers=headers)
        print(response.text)

        Assertions.assert_status_code(response, 200)
        # Метод работает с JSON ответом, ищет значение по ключу и сравнивает его с ожидаемым
        Assertions.assert_json_value_by_name(response, 'platform', user_agent_platform[0],
                                             "the platform is not correctly defined")

    user_agent_browser = [
        ("Chrome", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"),
        ("Firefox", 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0'),
        ("No", "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X)"
               " AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    ]

    @pytest.mark.parametrize("user_agent_browser", user_agent_browser)
    @allure.description("Test check user agent - device")
    def test_check_user_agent_browser(self, user_agent_browser):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        headers = {"User-Agent": user_agent_browser[1]}

        response = MyRequests.get(url=url, headers=headers)

        Assertions.assert_status_code(response, 200)
        # Метод работает с JSON ответом, ищет значение по ключу и сравнивает его с ожидаемым
        Assertions.assert_json_value_by_name(response, 'browser', user_agent_browser[0],
                                             "the browser is not correctly defined")
