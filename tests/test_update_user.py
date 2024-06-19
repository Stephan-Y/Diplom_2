from data import *
import allure
import pytest
import requests
from data import NewUser


class TestUpdateUser:

    @allure.title('Проверка изменения почты и/или имени у авторизованного пользователя на корректную почту и/или имя')
    @pytest.mark.parametrize('new_user_data', [NewUser.gen_new_user_name,
                                               NewUser.gen_new_user_email,
                                               NewUser.gen_new_user_email_and_name])
    def test_update_user_name(self, gen_new_user_data, new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        updated_user = requests.patch(url=Url.UPDATE_USER, headers={'Authorization': token}, data=new_user_data)
        assert updated_user.status_code == 200 and updated_user.json()['user'] == new_user_data, (
            f"Фактический результат: {updated_user.status_code}, {updated_user.json()['user']}")

    @allure.title('Проверка изменения пароля у авторизованного пользователя')
    def test_update_user_password(self, gen_new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        updated_user = requests.patch(url=Url.UPDATE_USER, headers={'Authorization': token},
                                      data={'password': 'new_password'})
        assert updated_user.status_code == 200 and updated_user.json()['success'] is True, (
            f"Фактический результат: {updated_user.status_code}, {updated_user.json()}")

    @allure.title('Проверка изменения пароля, имени, почты у не авторизованного пользователя')
    @pytest.mark.parametrize('new_user_incorrect_data', [
        NewUser.gen_new_user_name,
        NewUser.gen_new_user_email,
        NewUser.gen_new_user_email_and_name,
        UserTestData.gen_new_user_no_name(),
        UserTestData.gen_new_user_empty_name(),
        UserTestData.gen_new_user_no_email(),
        UserTestData.gen_new_user_empty_email(),
        UserTestData.gen_new_user_no_password(),
        UserTestData.gen_new_user_empty_password()
    ])
    def test_update_not_auth_user(self, gen_new_user_data, new_user_incorrect_data):
        updated_user = requests.patch(url=Url.UPDATE_USER,
                                      data=new_user_incorrect_data)
        print(updated_user.json())
        assert updated_user.status_code == 401 and updated_user.json()['message'] == Error.NOT_AUTHORIZED_401, (
            f"Фактический результат: {updated_user.status_code}, "
            f"{updated_user.json()['success']},"
            f"{updated_user.json()['message']}")
