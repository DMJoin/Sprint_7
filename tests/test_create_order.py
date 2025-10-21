import requests
import pytest
import allure
from datasets import *
from urls import BASE_URL

class TestCreateOrder:

    @allure.title('Возможность сделать заказ самоката разных доступных цветов')
    @pytest.mark.parametrize('color', available_colors)
    def test_create_order_with_different_colors(self, color):
        payload = color
        response = requests.post(f'{BASE_URL}/orders', json=payload)
        assert response.status_code == 201
        assert "track" in response.json()
     