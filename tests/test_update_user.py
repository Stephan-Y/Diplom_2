import json

from data import *
import allure
import pytest
import requests
from data import NewUser


class TestUpdateUser:

    @allure.title('Проверка изменения данных у авторизованного пользователя на корректную почту и имя')
    @pytest.mark.parametrize('new_user_data', [NewUser.gen_new_user_name,
                                               NewUser.gen_new_user_email,
                                               NewUser.gen_new_user_email_and_name])
    def test_update_user_name(self, gen_new_user_data, new_user_data):
        token = str(gen_new_user_data.json()['accessToken'])
        updated_user = requests.patch(url=Url.UPDATE_USER, headers= {'Authorization': token}, data=new_user_data)
        assert updated_user.status_code == 200 and updated_user.json()['user'] == new_user_data, (
            f"Фактический результат: {updated_user.status_code}, {updated_user.json()['user']}")
