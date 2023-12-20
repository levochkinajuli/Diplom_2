import pytest
import string
import random
import requests


@pytest.fixture(scope="function")
def user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(4)}@ya.ru'
    password = generate_random_string(5)
    name = generate_random_string(5)

    user_data = {
        "email": email,
        "password": password,
        "name": name
    }

    yield user_data

    url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    data = {"email": user_data["email"], "password": user_data["password"]}
    response = requests.post(url, json=data)
    token = response.json().get("accessToken")

    if token:
        delete_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
        headers = {'Authorization': token}
        delete_response = requests.delete(delete_url, headers=headers)

        assert delete_response.status_code == 202


@pytest.fixture(scope="function")
def token():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(4)}@ya.ru'
    password = generate_random_string(5)
    name = generate_random_string(5)

    url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    data = {"email": email, "password": password, "name": name}
    response = requests.post(url, json=data)

    assert response.status_code == 200

    token = response.json().get("accessToken")

    yield token

    delete_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    headers = {'Authorization': token}
    delete_response = requests.delete(delete_url, headers=headers)

    assert delete_response.status_code == 202


# @pytest.fixture(scope="function")
# def order():
#     def generate_random_string(length):
#         letters = string.ascii_lowercase
#         random_string = ''.join(random.choice(letters) for i in range(length))
#         return random_string
#
#     email = f'{generate_random_string(4)}@ya.ru'
#     password = generate_random_string(5)
#     name = generate_random_string(5)
#
#     url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
#     data = {"email": email, "password": password, "name": name}
#     response = requests.post(url, json=data)
#
#     assert response.status_code == 200
#
#     token = response.json().get("accessToken")
#
#     yield token
#
#     delete_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
#     headers = {'Authorization': token}
#     delete_response = requests.delete(delete_url, headers=headers)
#
#     assert delete_response.status_code == 202
