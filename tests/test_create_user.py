import allure
import pytest
from lib.base_class import BaseClass
from lib.assertions import Assertions
from lib.my_request import MyRequests


@allure.epic("Create user")
class TestCreateUser(BaseClass):

    @allure.step("Get random data")
    def get_random_data(self):
        """Получение данных для регистрации вынесено отдельно для генерации новых данных в каждом тесте"""
        random_data = BaseClass.random_data('ru')
        data = {"password": random_data["password"],
                "username": random_data["user_name"],
                "firstName": random_data["first_name"],
                "lastName": random_data["last_name"],
                "email": random_data["email"]}
        return data

    @allure.description("Test create user successfully")
    def test_create_user_successfully(self):
        """Регистрация нового пользователя используя уникальные данные"""
        data = self.get_random_data()
        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Test create user with existing email")
    def test_create_user_with_existing_email(self):
        """Регистрация пользователя с существующей электронной почтой"""
        data = self.get_random_data()
        email = "vinkotov@example.com"
        data["email"] = email

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            'utf-8') == f"Users with email '{email}' already exists", f'unexpected response {response.content}'

    @pytest.mark.parametrize("field", ["password", "username", "firstName", "lastName", "email"])
    @pytest.mark.parametrize("invalid_data", ['', 's', 'absent', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])
    @allure.description("Test registration of a new user with invalid data")
    def test_create_user_with_invalid_data(self, field, invalid_data):
        """
        Тестирование регистрации с некорректными данными
        В параметризации определяем поля которые будем тестировать и тестовые данные
        Тестовые данные для проверки:
            Тест регистрации с пустым полем,
            тест регистрации с полем из 1 символа,
            тест регистрации с полем более 250 символов,
            тест регистрации без обязательного поля
        """
        test_data = self.get_random_data()

        if invalid_data == 'absent':
            test_data.pop(field)  # удаляем необходимое поле из данных для регистрации
        else:
            test_data[field] = invalid_data  # редактируем необходимое поле из данных для регистрации

        response = MyRequests.post('/user/', data=test_data)

        Assertions.assert_status_code(response, 400)  # ожидаем ошибку
