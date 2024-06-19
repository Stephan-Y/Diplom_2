from helpers import UserTestData


class Url:
    URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_USER = URL + '/api/auth/login'
    LOGOUT_USER = URL + '/api/auth/logout'
    CREATE_USER = URL + '/api/auth/register'
    REGISTER_USER = URL + '/api/auth/register'
    UPDATE_USER = URL + '/api/auth/user'
    GET_USER = URL + '/api/auth/user'
    MAKE_ORDER = URL + '/api/orders'
    GET_INGREDIENTS = URL + '/api/ingredients'


class Error:
    USER_ALREADY_EXISTS_403 = 'User already exists'
    FIELDS_REQUIRED_403 = 'Email, password and name are required fields'
    INCORRECT_401 = 'email or password are incorrect'
    NOT_AUTHORIZED_401 = 'You should be authorised'
    EMAIL_ALREADY_EXISTS_403 = 'User with such email already exists'
    NO_INGREDIENT_400 = 'Ingredient ids must be provided'
    INCORRECT_HASH = 'test-hash'


class Ingredient:
    LIGHT_BURGER = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    INCORRECT_BURGER = {"ingredients": ["61c0c5INCORRECT1bdaaa6d", "61c0c5a71INCORRECTdaaa72"]}
    EMPTY_BURGER = {"ingredients": []}


class NewUser:
    gen_new_user_name = {'email': UserTestData.gen_email(),
                         'name': 'new' + UserTestData.gen_name()}
    gen_new_user_email = {'email': 'new' + UserTestData.gen_email(),
                          'name': UserTestData.gen_name()}
    gen_new_user_email_and_name = {'email': 'new' + UserTestData.gen_email(),
                                   'name': 'new' + UserTestData.gen_name()}
