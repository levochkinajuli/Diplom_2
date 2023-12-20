import requests


def list_of_ingredients():
    url = "https://stellarburgers.nomoreparties.site/api/ingredients"

    response = requests.get(url)
    ingredients_data = response.json()
    values = [d.get('_id') for d in ingredients_data['data']]
    return values
