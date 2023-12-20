import requests
from conftest import token, user


class TestChangeData:
    def test_login_user_change_name(self, token):
        user_token = token
        headers = {'Authorization': user_token}
        url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
        new_name = 'Mariya'
        data = {"name": new_name}
        response = requests.patch(url, headers=headers, json=data)
        assert response.status_code == 200

    def test_login_user_change_email(self, token):
        user_token = token
        headers = {'Authorization': user_token}
        url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
        new_email = 'masha1212@ya.ru'
        data = {"email": new_email}
        response = requests.patch(url, headers=headers, json=data)
        assert response.status_code == 200

    def test_login_user_change_password(self, token):
        user_token = token
        headers = {'Authorization': user_token}
        url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
        new_password = 'passemail'
        data = {"password": new_password}
        response = requests.patch(url, headers=headers, json=data)
        assert response.status_code == 200

    def test_user_change_data_without_login(self, user):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
        data = user
        requests.post(url, json=data)
        url_2 = 'https://stellarburgers.nomoreparties.site/api/auth/user'
        new_data = {"email": "boriska@ya.ru", "password": 'Antalia', "name": 'Boris'}
        response = requests.patch(url_2, json=new_data)
        assert response.status_code == 401
