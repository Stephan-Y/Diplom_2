from data import *
import allure
import requests


class TestGetUserOrder:

    @allure.title('Проверка получения заказа у авторизованного юзера')
    def test_get_order_auth_user(self, gen_new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        get_order = requests.get(url=Url.MAKE_ORDER, headers={'Authorization': token})
        assert get_order.json()['success'] is True and get_order.status_code == 200, (
            f"Фактический результат: {get_order.status_code}, {get_order.json()['success']}")


    @allure.title('Проверка невозможости получения заказа у не авторизованного юзера')
    def test_get_order_auth_user(self, gen_new_user_data):
        get_order = requests.get(url=Url.MAKE_ORDER, headers={'Authorization': ''})
        assert get_order.json()['success'] is False and get_order.status_code == 401, (
            f"Фактический результат: {get_order.status_code}, {get_order.json()['success']}")
