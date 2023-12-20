import requests
from conftest import user


class TestLoginUser:
    def test_login_exist_user(self, user):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
        data = user
        requests.post(url, json=data)
        url_2 = 'https://stellarburgers.nomoreparties.site/api/auth/login'
        data_to = {"email": data["email"], "password": data["password"]}
        response = requests.post(url_2, json=data_to)
        assert response.status_code == 200

    def test_login_incorrect_data(self, user):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
        data = user
        requests.post(url, json=data)
        url_2 = 'https://stellarburgers.nomoreparties.site/api/auth/login'
        data_to = {"email": f'123{data["email"]}', "password": f'123{data["password"]}'}
        response = requests.post(url_2, json=data_to)
        assert response.status_code == 401
