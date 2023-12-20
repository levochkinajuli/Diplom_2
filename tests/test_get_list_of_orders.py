import requests
from ingredients import list_of_ingredients
from conftest import token


class TestGetOrders:
    def test_get_order_authorized(self, token):
        user_token = token
        ing = list_of_ingredients()
        headers = {'Authorization': user_token}
        url = 'https://stellarburgers.nomoreparties.site/api/orders'
        data = {"ingredients": [ing[5], ing[4]]}
        requests.post(url, headers=headers, json=data)
        url_2 = 'https://stellarburgers.nomoreparties.site/api/orders'
        response = requests.get(url_2, headers=headers)
        orders_count = response.json().get("orders")
        assert response.status_code == 200
        assert len(orders_count) == 1

    def test_get_order_not_authorized(self):
        url = 'https://stellarburgers.nomoreparties.site/api/orders'
        response = requests.get(url)
        assert response.status_code == 401

    def test_get_all_orders(self):
        url = 'https://stellarburgers.nomoreparties.site/api/orders/all'
        response = requests.get(url)
        orders_count = response.json().get("orders")
        assert response.status_code == 200
        assert 'totalToday' in response.text
        assert len(orders_count) == 50
