import pytest
import requests
from data import *
from helpers import UserTestData


@pytest.fixture
def gen_new_user_data():
    response = requests.post(Url.CREATE_USER, data=UserTestData.gen_new_user())
    yield response
    token = str(response.json()['accessToken'])
    requests.delete(Url.UPDATE_USER, headers={'Authorization': token})


@pytest.fixture
def gen_new_user_and_register():
    user_data = UserTestData.gen_new_user()
    response = requests.post(Url.REGISTER_USER, data=user_data)
    token = str(response.json()['accessToken'])
    yield user_data
    requests.delete(Url.UPDATE_USER, headers={'Authorization': token})
