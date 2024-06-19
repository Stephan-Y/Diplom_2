from data import *
import allure
import pytest
import requests
from helpers import UserTestData


class TestRegisterUser:

    @allure.title('Тест создание нового пользователя')
    def test_create_new_user(self, gen_new_user_data):
        assert gen_new_user_data.status_code == 200 and gen_new_user_data.json()['success'] is True, (
            f"Фактический результат: {gen_new_user_data.status_code}, {gen_new_user_data.json()['success']}"
        )

    @allure.title('Тестирование не возможности повторно зарегистрировать существующего пользователя')
    def test_create_old_user(self, gen_new_user_data):
        response = requests.post(Url.CREATE_USER, data=UserTestData.gen_new_user())
        expected_response = {"success": False, "message": Error.USER_ALREADY_EXISTS_403}
        assert response.status_code == 403 and response.json() == expected_response, (
            f"Фактический результат: {gen_new_user_data.status_code}, {gen_new_user_data.json()['success']}")

    @allure.title(
        'Тестирование невозможности создания пользвателя с незаполненным или отсутствующем обязательным полем')
    @pytest.mark.parametrize('incorrect_user', [
        UserTestData.gen_new_user_no_name(),
        UserTestData.gen_new_user_empty_name(),
        UserTestData.gen_new_user_no_email(),
        UserTestData.gen_new_user_empty_email(),
        UserTestData.gen_new_user_no_password(),
        UserTestData.gen_new_user_empty_password()
    ])
    def test_create_incorrect_user(self, incorrect_user):
        response = requests.post(Url.CREATE_USER, data=incorrect_user)
        expected_response = {"success": False, "message": Error.FIELDS_REQUIRED_403}
        assert response.status_code == 403 and response.json() == expected_response, (
            f"Фактический результат: {response.status_code}, {response.json()}")
