import requests
from ingredients import list_of_ingredients
from conftest import token


class TestMakeOrder:
    def test_make_order_correct_ing_no_auth(self):
        ing = list_of_ingredients()
        url = 'https://stellarburgers.nomoreparties.site/api/orders'
        data = {"ingredients": [ing[0], ing[7]]}
        response = requests.post(url, json=data)
        assert response.status_code == 200

    def test_make_order_no_ing(self):
        url = 'https://stellarburgers.nomoreparties.site/api/orders'
        response = requests.post(url)
        assert response.status_code == 400

    def test_make_order_incorrect_ing_id(self):
        url = 'https://stellarburgers.nomoreparties.site/api/orders'
        data = {"ingredients": [9876, 9845]}
        response = requests.post(url, json=data)
        assert response.status_code == 500

    def test_make_order_correct_ing_auth(self, token):
        ing = list_of_ingredients()
        user_token = token
        headers = {'Authorization': user_token}
        url = 'https://stellarburgers.nomoreparties.site/api/orders'
        data = {"ingredients": [ing[8], ing[2]]}
        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 200
