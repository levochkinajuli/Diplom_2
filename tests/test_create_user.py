import requests
from conftest import user


class TestCreateUser:
    def test_create_user(self, user):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
        data = user
        response = requests.post(url, json=data)
        assert response.status_code == 200

    def test_create_the_same_user(self, user):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
        data = user
        response = requests.post(url, json=data)
        assert response.status_code == 200
        response_2 = requests.post(url, json=data)
        assert response_2.status_code == 403
        assert "User already exists" in response_2.text

    def test_create_user_without_one_field(self, user):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
        data = user
        data_to = {"email": data["email"], "password": data["password"]}
        response = requests.post(url, json=data_to)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.text
