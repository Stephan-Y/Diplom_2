import random
from datetime import datetime


class UserTestData:

    @staticmethod
    def gen_name():
        name = "StepanTest_" + datetime.now().strftime("%Y_%m_%d_%H_%M")
        return name

    @staticmethod
    def gen_email():
        email = UserTestData.gen_name() + "@yandex.ru"
        return email

    @staticmethod
    def gen_password():
        password = f"Stepan_{random.randint(99, 999)}"
        return password

    @staticmethod
    def gen_new_user():
        user_data = {
            "email": UserTestData.gen_email(),
            "password": UserTestData.gen_password(),
            "name": UserTestData.gen_name()
        }
        return user_data

    @staticmethod
    def gen_new_user_no_email():
        user_data = {"password": UserTestData.gen_password(),
                     "name": UserTestData.gen_name()}
        return user_data

    @staticmethod
    def gen_new_user_no_password():
        user_data = {"email": UserTestData.gen_email(),
                     "name": UserTestData.gen_name()}
        return user_data

    @staticmethod
    def gen_new_user_no_name():
        user_data = {"email": UserTestData.gen_email(), "password": UserTestData.gen_password()}
        return user_data

    @staticmethod
    def gen_new_user_empty_name():
        user_data = {"email": UserTestData.gen_email(), "password": UserTestData.gen_password(),
                     "name": ""}
        return user_data

    @staticmethod
    def gen_new_user_empty_password():
        user_data = {"email": UserTestData.gen_email(), "password": "",
                     "name": UserTestData.gen_name()}
        return user_data

    @staticmethod
    def gen_new_user_empty_email():
        user_data = {"email": "", "password": UserTestData.gen_password(),
                     "name": UserTestData.gen_name()}
        return user_data
