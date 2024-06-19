import json
from data import *
import allure
import requests


class TestLoginUser:

    @allure.title('Проверка корректного логирования зарегистрированного пользователя')
    def test_login_correct_user_data(self, gen_new_user_and_register):
        user = gen_new_user_and_register
        payload = {
            "email": user.get("email"),
            "password": user.get("password")
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Url.LOGIN_USER, headers=headers, data=json.dumps(payload))
        assert response.json()['success'] == True and response.status_code == 200, (
            f'Фактический результат: {response.status_code}, {response.json()["success"]}'
        )

    @allure.title('Проверка логирования зарегистрированного пользователя с некорректной почтой')
    def test_login_incorrect_email(self, gen_new_user_and_register):
        user = gen_new_user_and_register
        payload = {
            "email": user.get("email") + '1',
            "password": user.get("password")
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Url.LOGIN_USER, headers=headers, data=json.dumps(payload))
        expected_result = {'success': False, 'message': Error.INCORRECT_401}
        assert response.status_code == 401 and response.json() == expected_result, (
            f'Фактический результат: {response.status_code}, {response.json()["success"]}, {response.json()["message"]}')


    @allure.title('Проверка логирования зарегистрированного пользователя с некорректным паролем')
    def test_login_incorrect_password(self, gen_new_user_and_register):
        user = gen_new_user_and_register
        payload = {
            "email": user.get("email"),
            "password": user.get("password") + '1'
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Url.LOGIN_USER, headers=headers, data=json.dumps(payload))
        expected_result = {'success': False, 'message': Error.INCORRECT_401}
        assert response.status_code == 401 and response.json() == expected_result, (
            f'Фактический результат: {response.status_code}, {response.json()["success"]}, {response.json()["message"]}')