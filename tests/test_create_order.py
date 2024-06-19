from data import *
import allure
import requests


class TestCreateOrder:

    @allure.title('Проверка заказа на авторизованном юзере')
    def test_make_correct_order_auth_user(self, gen_new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        make_order = requests.post(url=Url.MAKE_ORDER, headers={'Authorization': token}, json=Ingredient.LIGHT_BURGER)
        assert make_order.json()['success'] is True and make_order.status_code == 200, (
            f'Фактический результат: {make_order.status_code}, {make_order.json()["success"]}'
        )

    @allure.title('Проверка невозможности заказа бургера с неверным хэшем на авторизованном юзере')
    def test_make_incorrect_order_auth_user(self, gen_new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        make_order = requests.post(url=Url.MAKE_ORDER, headers={'Authorization': token}, json=Ingredient.INCORRECT_BURGER)
        print(make_order.text)
        assert make_order.status_code == 500, (
            f'Фактический результат: {make_order.status_code}')

    @allure.title('Проверка заказа пустого бургера на авторизованном юзере')
    def test_make_empty_burger_order_auth_user(self, gen_new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        make_order = requests.post(url=Url.MAKE_ORDER, headers={'Authorization': token}, json=Ingredient.EMPTY_BURGER)
        assert make_order.json()['success'] is False and make_order.status_code == 400, (
            f'Фактический результат: {make_order.status_code}, {make_order.json()["success"]}'
        )
